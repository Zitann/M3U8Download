# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'M3U8Download.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_M3U8Download(object):
    def setupUi(self, M3U8Download):
        if not M3U8Download.objectName():
            M3U8Download.setObjectName(u"M3U8Download")
        M3U8Download.resize(400, 272)
        M3U8Download.setMinimumSize(QSize(400, 272))
        M3U8Download.setMaximumSize(QSize(400, 300))
        self.widget = QWidget(M3U8Download)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-1, -1, 401, 301))
        self.widget.setMinimumSize(QSize(401, 301))
        self.widget.setMaximumSize(QSize(401, 301))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 71, 31))
        self.label.setMinimumSize(QSize(71, 31))
        self.label.setMaximumSize(QSize(71, 31))
        self.m3u8_url = QLineEdit(self.widget)
        self.m3u8_url.setObjectName(u"m3u8_url")
        self.m3u8_url.setGeometry(QRect(110, 30, 261, 31))
        self.m3u8_url.setMinimumSize(QSize(261, 31))
        self.m3u8_url.setMaximumSize(QSize(261, 31))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 90, 131, 31))
        self.label_2.setMinimumSize(QSize(131, 31))
        self.label_2.setMaximumSize(QSize(131, 31))
        self.file_name = QLineEdit(self.widget)
        self.file_name.setObjectName(u"file_name")
        self.file_name.setGeometry(QRect(160, 89, 211, 31))
        self.file_name.setMinimumSize(QSize(211, 31))
        self.file_name.setMaximumSize(QSize(211, 31))
        self.set_dir = QPushButton(self.widget)
        self.set_dir.setObjectName(u"set_dir")
        self.set_dir.setGeometry(QRect(30, 140, 111, 41))
        self.set_dir.setMinimumSize(QSize(111, 41))
        self.set_dir.setMaximumSize(QSize(111, 41))
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 140, 171, 41))
        self.label_3.setMinimumSize(QSize(171, 41))
        self.label_3.setMaximumSize(QSize(171, 41))
        self.download = QPushButton(self.widget)
        self.download.setObjectName(u"download")
        self.download.setGeometry(QRect(30, 200, 341, 51))
        self.download.setMinimumSize(QSize(341, 51))
        self.download.setMaximumSize(QSize(341, 51))

        self.retranslateUi(M3U8Download)

        QMetaObject.connectSlotsByName(M3U8Download)
    # setupUi

    def retranslateUi(self, M3U8Download):
        M3U8Download.setWindowTitle(QCoreApplication.translate("M3U8Download", u"M3U8Download", None))
        self.label.setText(QCoreApplication.translate("M3U8Download", u"M3U8  URL", None))
        self.label_2.setText(QCoreApplication.translate("M3U8Download", u"\u4fdd\u5b58\u6587\u4ef6\u540d\uff08\u53ef\u4e0d\u586b\uff09", None))
        self.set_dir.setText(QCoreApplication.translate("M3U8Download", u"\u9009\u62e9\u4fdd\u5b58\u7684\u76ee\u5f55", None))
        self.label_3.setText(QCoreApplication.translate("M3U8Download", u"\u9ed8\u8ba4\u4fdd\u5b58\u5230\u5f53\u524d\u76ee\u5f55\u7684videos\u4e2d", None))
        self.download.setText(QCoreApplication.translate("M3U8Download", u"\u4e0b\u8f7d", None))
    # retranslateUi

