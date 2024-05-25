# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(800, 600)
        self.pic_label = QLabel(main)
        self.pic_label.setObjectName(u"pic_label")
        self.pic_label.setGeometry(QRect(100, 20, 400, 300))
        self.pic_label.setScaledContents(True)
        self.pic_label.setAlignment(Qt.AlignCenter)
        self.scan_pic = QPushButton(main)
        self.scan_pic.setObjectName(u"scan_pic")
        self.scan_pic.setGeometry(QRect(10, 530, 211, 51))
        font = QFont()
        font.setPointSize(16)
        self.scan_pic.setFont(font)
        self.pic_list = QListWidget(main)
        self.pic_list.setObjectName(u"pic_list")
        self.pic_list.setGeometry(QRect(380, 390, 401, 192))
        self.log_text = QTextBrowser(main)
        self.log_text.setObjectName(u"log_text")
        self.log_text.setGeometry(QRect(540, 60, 251, 301))
        self.label = QLabel(main)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(380, 350, 121, 31))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(main)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(610, 20, 121, 31))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.ip_text = QLineEdit(main)
        self.ip_text.setObjectName(u"ip_text")
        self.ip_text.setGeometry(QRect(10, 380, 201, 41))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(20)
        self.ip_text.setFont(font1)
        self.label_3 = QLabel(main)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 340, 181, 31))
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.tcp_rec = QPushButton(main)
        self.tcp_rec.setObjectName(u"tcp_rec")
        self.tcp_rec.setGeometry(QRect(10, 440, 211, 51))
        self.tcp_rec.setFont(font)
        self.label_4 = QLabel(main)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 370, 121, 211))
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"\u53d8\u7535\u7ad9\u5de1\u68c0\u4e0a\u4f4d\u673a", None))
        self.pic_label.setText(QCoreApplication.translate("main", u"\u56fe\u7247\u663e\u793a\u533a\u57df", None))
        self.scan_pic.setText(QCoreApplication.translate("main", u"\u5237\u65b0\u56fe\u7247\u5217\u8868", None))
        self.label.setText(QCoreApplication.translate("main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">\u56fe\u7247\u5217\u8868</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">\u65e5\u5fd7\u8f93\u51fa</span></p></body></html>", None))
        self.ip_text.setText(QCoreApplication.translate("main", u"192.168.1.170", None))
        self.label_3.setText(QCoreApplication.translate("main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">\u8bf7\u8f93\u5165ip\u5730\u5740</span></p></body></html>", None))
        self.tcp_rec.setText(QCoreApplication.translate("main", u"\u63a5\u6536\u56fe\u7247", None))
        self.label_4.setText(QCoreApplication.translate("main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">\u5524\u9192\u8bcd</span></p><p align=\"center\"><span style=\" font-size:16pt;\">\u94c1\u86cb\u94c1\u86cb</span></p><p align=\"center\"><span style=\" font-size:16pt;\">\u8bed\u97f3\u547d\u4ee4</span></p><p align=\"center\"><span style=\" font-size:16pt;\">\u5f00\u59cb\u5de1\u68c0</span></p><p align=\"center\"><span style=\" font-size:16pt;\">\u4f20\u8f93\u56fe\u7247</span></p></body></html>", None))
    # retranslateUi

