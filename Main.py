#coding=utf-8
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
import time
import cv2
import csv
import numpy as np
from retinaface import Retinaface
import extract_name
import compare
from SelectPic import pick_video
from SelectPic import pick_pic
from SelectPic import encode_pic
import sys
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import *
import predict_pic
import predict_video
from LoginWindow import Ui_loginWindow
from SelectPic import FilePicker

class LoginWindow(QMainWindow,Ui_loginWindow):
    def __init__(self):
        super().__init__()
        # 继承外部ui
        self.setupUi(self)
        # 隐藏外部多余窗口 他们要一起写上
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # 主窗体阴影
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(0,0)
        self.shadow.setBlurRadius(15)
        self.shadow.setColor(QtCore.Qt.blue)
        self.frame_1.setGraphicsEffect(self.shadow)
        self.frame_2.setGraphicsEffect(self.shadow)
        # 主按钮绑定事件
        self.stackedWidget_login.setCurrentIndex(1)
        self.pushButton_login.clicked.connect(lambda :self.stackedWidget_login.setCurrentIndex(1))
        self.pushButton_register.clicked.connect(lambda :self.stackedWidget_login.setCurrentIndex(0))
        self.pushButton_sure.clicked.connect(self.verify_login)
        self.pushButton_r_register.clicked.connect(self.register_submit)

    def register_submit(self):
        account = self.lineEdit_r_account.text()
        pwd1 = self.lineEdit_r_pwd.text()
        pwd2 = self.lineEdit_r_pwd2.text()

        # 检查密码是否一致
        if pwd1 != pwd2:
            self.label_message.setText('两次输入的密码不一样')
            return

        # 将账户和密码写入 CSV 文件
        csv_file = 'user_accounts.csv'
        with open(csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([account, pwd1])

        self.label_message.setText('注册成功')



        # 自定义内部ui
        self.setup_ui()

    def verify_login(self):
        account = self.lineEdit_account.text()
        pwd = self.lineEdit_pwd.text()

        # 从 CSV 文件中读取账户和密码信息
        csv_file = 'user_accounts.csv'
        with open(csv_file, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == account and row[1] == pwd:
                    print('登录成功')
                    try:
                        self.main = FilePicker()
                        self.main.show()
                        self.close()
                    except Exception as e:
                        print(e)
                    return

        # 如果账户或密码错误，则显示错误消息
        self.label_message.setText('账号或密码错误，请重试')

    def setup_ui(self):
        pass


# 主界面类
class MianWindow(QMainWindow,FilePicker):
    def __init__(self):
        super().__init__()
        self.ui = FilePicker()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
    predict_pic.detect_pic(pick_pic())
    # predict_video.detect_video(pick_video())



