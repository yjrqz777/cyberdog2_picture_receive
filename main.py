import sys
import os
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget,QMessageBox,QFileDialog,QListWidget
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QColorDialog ,QMessageBox,QLabel  
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
from PySide6.QtGui import QPixmap
from mainui_ui import Ui_main as Ui_MainWindow
import random
# from untitled2_ui import Ui_MainWindow111 as Ui_MainWindow2
import socket  
import cv2  # OpenCV库用于保存图片  
import numpy as np  # numpy库用于处理字节流
import threading
# 创建一个socket对象  

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

# host = '127.0.0.1'
# port = 11000  # 设置端口号，与发送端一致  
# s.connect((host, port))  
# 接收图片字节流的长度  


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.setupUi(self)
        self.bind_slots()
        self.log_text.append('hello')
        self.pic_list.itemSelectionChanged.connect(self.item_clicked)
        # QListWidgetItem('Text Item 1', listWidget)
        #使用addItem添加条目
        self.pic_list.addItem('Text ')
        # self.ui.no.clicked.connect(self.no_click)
    def log(self,text):
        self.log_text.append(text)

    def tcplink(self,host, port):  
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        # host = socket.gethostname()  
        # host = '127.0.0.1'
        # port = 11000  
        # server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 连接服务，指定主机和端口  
        # server_socket.bind((host, port)) 
        self.log('{}{}'.format(host,port)) 
        # 设置最大连接数  
        # server_socket.listen(5)  
        self.log(f'等待连接') 
        # client_socket.connect((host, port)) 
        # self.log(f'连接成功') 
        flag = True
        try:
            client_socket.connect((host, port)) 
            flag = True
            self.log('连接成功')

            while True:  
                # self.log(f'Connected by {addr}')  
                # 接收图片文件名  
                filename = client_socket.recv(1024).decode('utf-8').strip()  
                if filename == None or filename == '':  
                    break
                # 接收文件大小（可选）  
                filesize = int.from_bytes(client_socket.recv(8), byteorder='big')  
        
                # 接收图片数据并保存  
                self.log(f'{filename}') 
                if not os.path.exists("picture"):  
                    os.mkdir("picture")
                with open("./picture/"+filename, 'wb') as f:  
                    while filesize > 0:  
                        data = client_socket.recv(4096)  
                        f.write(data)  
                        filesize -= len(data)  
                self.log(f'已接收{filename}')
            client_socket.close()
        except Exception as e:
            flag = False
            self.log(f'连接失败{e}')
            # client_socket.close()
            # print(e)


    def item_clicked(self):
            
            item = self.pic_list.currentItem()
            # self.log(item.text())
            self.pic_label.setPixmap(QPixmap(f'./picture/{item.text()}'))
            # self.label_result.setText(f"你选择的编程语言为 : "+ str(item.text()))
    def open_pic(self):
        self.pic_list.clear()
        self.log('open_pic')
        # file_path = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.gif)")
        directory = './picture/'  
        # 使用os.listdir()函数来获取目录下的所有文件和文件夹  
        files_and_directories = os.listdir(directory)  
        
        # 打印出所有文件和文件夹  
        for item in files_and_directories:  
            self.pic_list.addItem(item)
            # self.log(item)
    def recv_image(self):
        ip = self.ip_text.text()
        # self.log(ip)
        self.log('recv_image')
        t=threading.Thread(target=self.tcplink,args=(ip, 11000))
        t.setDaemon(True)  # <-- add this
        t.start()

    def bind_slots(self):
        self.scan_pic.clicked.connect(self.open_pic)
        self.tcp_rec.clicked.connect(self.recv_image)

    # def yes_click(self,):
    #     reply = QMessageBox.question(self, '????', "确认？",
    #                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    #     if reply == QMessageBox.Yes:
    #         self.close()  
    #     self.log('Yes')



    # def closeEvent(self,a0: QtGui.QCloseEvent) -> None:
    #     reply = QMessageBox.question(self, '????', "确认？",
    #                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    #     if reply == QMessageBox.Yes:
    #         a0.accept() 
    #     else:
    #         a0.ignore()



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()

    sys.exit(app.exec())