from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import QRunnable, QThreadPool, Signal, Slot

from M3U8Download import M3U8Download
from M3U8Download_ui import Ui_M3U8Download
class Worker(QRunnable):
    def __init__(self,url,path,name,parent) -> None:
        
        super().__init__()
        self.parent = parent
        if name == '' and path == '':
            self.m3u8 = M3U8Download(url)
        elif name == '' and path != '':
            self.m3u8 = M3U8Download(url, path=path)
        elif name != '' and path == '':
            self.m3u8 = M3U8Download(url, name=name)
        else:
            self.m3u8 = M3U8Download(url, path, name)

    def run(self):
        self.m3u8.run()
        self.parent.download.setEnabled(True)
        self.parent.download.setText('下载完成')
        

class M3U8DownloadGUI(QMainWindow, Ui_M3U8Download):
    dir = ''
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('M3U8Download')
        self.set_dir.clicked.connect(self.set_dir_clicked)
        self.download.clicked.connect(self.download_clicked)

    def set_dir_clicked(self):
        dir = QFileDialog.getExistingDirectory(self, '选择文件夹', './')
        self.dir = dir

    def download_clicked(self):
        url = self.m3u8_url.text()
        name = self.file_name.text()
        path = self.dir
        
        self.download.setEnabled(False)
        self.download.setText('下载中')
        if url == '':
            QMessageBox.warning(self, '警告', '请输入m3u8文件地址')
            return
        runnable = Worker(url, path, name, self)
        runnable.setAutoDelete(True)
        QThreadPool.globalInstance().start(runnable)

if __name__ == '__main__':
    app = QApplication()
    m3u8_download_gui = M3U8DownloadGUI()
    m3u8_download_gui.show()
    app.exec()
