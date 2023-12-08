import requests
import os
import asyncio
import aiofiles
import httpx
import sys

class M3U8Download:
    ts_list = []
    ffmpeg_path = os.path.join(os.getcwd(), 'ffmpeg.exe')
    def __init__(self, url, path=os.path.join(os.getcwd(), 'videos'), name='default'):
        self.url = url
        self.path = path
        if name:
            self.name = name
        if self.name == 'default':
            self.name = self.url.split('/')[-1].split('.')[0]
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        os.chdir(self.path)
        self.get_ts_list()

    def get_ts_list(self):
        if self.url:
            r = requests.get(self.url)
            with open(f'{self.name}.m3u8', 'w') as f:
                for line in r.text.split('\n'):
                    if line.startswith('#EXT-X-KEY'):
                        key = line.split('"')[1]
                        key_url = self.url[:self.url.rfind('/')+1] + key
                        key_r = requests.get(key_url)
                        key_path = key.split('/')[-1]
                        with open(key_path, 'wb') as key_f:
                            key_f.write(key_r.content)
                        line = line.replace(key, key_path)
                        f.write(line+'\n')
                        continue
                    if line.endswith('.ts'):
                        line = line.strip()
                        if line.startswith('http'):
                            self.ts_list.append(line)
                        else:
                            host = self.url[:self.url.rfind('/')+1]
                            line = host + line
                            self.ts_list.append(line)
                    line = line[line.rfind('/')+1:]
                    f.write(line+'\n')
        else:
            print('url is empty')
            exit()

        if not self.ts_list:
            print('ts_list is empty')
            exit()

    async def download_one(self, client,ts,semaphore):
        async with semaphore:
            async with client.stream('GET', ts) as r:
                if r.status_code == 200:
                    print(os.path.join(self.path, ts.split('/')[-1]))
                    async with aiofiles.open(ts.split('/')[-1], 'wb') as f:
                        async for chunk in r.aiter_bytes():
                            await f.write(chunk)
                else:
                    print(f'{ts} download failed')

    async def download_all(self):
        # 设置最大连接数
        semaphore = asyncio.Semaphore(16)
        async with httpx.AsyncClient(timeout=httpx.Timeout(30.0), limits=httpx.Limits(max_connections=1000)) as client:
            tasks = [self.download_one(client,ts,semaphore) for ts in self.ts_list]
            await asyncio.gather(*tasks)



    def to_mp4(self):
        if os.path.exists(f'{self.name}.mp4'):
            os.remove(f'{self.name}.mp4')
        os.system(f'{self.ffmpeg_path} -allowed_extensions ALL -i {self.name}.m3u8 -c copy {self.name}.mp4')
        os.system(f'del {self.name}.m3u8 *.ts *.key')


    
    def run(self):
        asyncio.run(self.download_all())
        self.to_mp4()

if __name__ == '__main__':

    command_line_arguments = sys.argv[1:]
    if len(command_line_arguments) == 0:
        print('使用--help查看帮助')
        exit()
    if command_line_arguments[0] == '--help':
        print('''
        使用方法：
        python M3U8Download.py [url] -n [name] -p [path]
        url: m3u8文件地址
        path: 保存路径
        name: 保存文件名
        ''')
        exit()
    if len(command_line_arguments) == 1:
        url = command_line_arguments[0]
        m3u8 = M3U8Download(url)
        m3u8.run()
    elif len(command_line_arguments) == 3:
        if command_line_arguments[1] == '-p':
            url = command_line_arguments[0]
            path = command_line_arguments[2]
            m3u8 = M3U8Download(url, path)
            m3u8.run()
        elif command_line_arguments[1] == '-n':
            url = command_line_arguments[0]
            name = command_line_arguments[2]
            m3u8 = M3U8Download(url, name=name)
            m3u8.run()
        else:
            print('使用--help查看帮助')
            exit()
    elif len(command_line_arguments) == 5:
        if command_line_arguments[1] == '-p' and command_line_arguments[3] == '-n':
            url = command_line_arguments[0]
            path = command_line_arguments[2]
            name = command_line_arguments[4]
            m3u8 = M3U8Download(url, path, name)
            m3u8.run()
        elif command_line_arguments[1] == '-n' and command_line_arguments[3] == '-p':
            url = command_line_arguments[0]
            path = command_line_arguments[4]
            name = command_line_arguments[2]
            m3u8 = M3U8Download(url, path, name)
            m3u8.run()
        else:
            print('使用--help查看帮助')
            exit()
    else:
        print('使用--help查看帮助')
        exit()