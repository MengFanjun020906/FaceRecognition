import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog,QPlainTextEdit,QVBoxLayout
import os

import predict_pic
import predict_video
from retinaface import Retinaface
import subprocess
from predict_video import detect_video
def pick_pic():
    app = QApplication(sys.argv)
    window = FilePicker()
    window.show()
    app.exec_()  # 执行Qt应用程序的事件循环
    return window.selected_file  # 返回选定的文件路径
    sys.exit(app.exec_())

def pick_video():
    app = QApplication(sys.argv)
    window = FilePicker()
    window.show()
    app.exec_()  # 执行Qt应用程序的事件循环
    return window.selected_mode
    sys.exit(app.exec_())

def encode_pic():
    app = QApplication(sys.argv)
    window = FilePicker()
    window.show()
    app.exec_()  # 执行Qt应用程序的事件循环
    sys.exit(app.exec_())



class FilePicker(QWidget):
    def __init__(self):
        super().__init__()
        self.selected_file = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('File Picker')
        self.setGeometry(100, 100, 300, 300)


        self.button_video = QPushButton('检测视频', self)
        self.button_video.setGeometry(100, 50, 100, 30)
        self.button_video.clicked.connect(self.openCam)

        self.pick_button = QPushButton('检测图片', self)
        self.pick_button.setGeometry(100, 100, 100, 30)
        self.pick_button.clicked.connect(self.pickFile)


        self.pick_button3 = QPushButton('编码人脸信息', self)
        self.pick_button3.setGeometry(100, 150, 100, 30)
        self.pick_button3.clicked.connect(self.encode)

        self.pick_button2 = QPushButton('录入人脸', self)
        self.pick_button2.setGeometry(100, 200, 100, 30)
        self.pick_button2.clicked.connect(self.TakePic)


        # self.setGeometry(100, 300, 600, 400)
        # self.output_text_edit = QPlainTextEdit()
        # self.output_text_edit.setReadOnly(True)  # 设置为只读模式
        #
        # layout = QVBoxLayout()
        # layout.addWidget(self.output_text_edit)
        #
        # central_widget = QWidget()
        # central_widget.setLayout(layout)
        # self.setCentralWidget(central_widget)
        #
        # # 在初始化期间添加示例输出信息
        # self.showOutput()

    def pickFile(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "All Files (*)", options=options)
        if file_name:
            # 设置选定的文件路径
            self.selected_file = file_name
            predict_pic.detect_pic(file_name)


    def openCam(self):
        video_path = 0
        video_save_path = ""
        video_fps = 25.0
        dir_origin_path = "img/"
        dir_save_path = "img_out/"
        predict_video.detect_video("video", video_path, video_save_path, video_fps, dir_origin_path, dir_save_path)
        # self.selected_mode = "video"
        #
        # self.close()

    def encode(self):
        retinaface = Retinaface(1)

        list_dir = os.listdir("face_dataset")
        image_paths = []
        names = []
        for name in list_dir:
            image_paths.append("face_dataset/" + name)
            names.append(name.split("_")[0])  # 根据下划线分割，只会取文件的名称而没有序号

        retinaface.encode_face_dataset(image_paths, names)
        print("编码完成")

    def TakePic(self):

        subprocess.Popen(['python3','TakePic.py'])

    # def showOutput(self):
    #     self.output_text_edit.appendPlainText("")
    #     self.output_text_edit.verticalScrollBar().setValue(self.output_text_edit.verticalScrollBar().maximum())


if __name__ == '__main__':
     file_path = pick_pic()
     print("选择的文件路径为:", file_path)

     # mode = pick_video()
     # print("模式为",mode)
