import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import subprocess

class ButtonClickApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Button Click App')
        self.setGeometry(100, 100, 400, 300)

        self.button_video = QPushButton('检测人脸', self)
        self.button_video.setGeometry(100, 100, 200, 50)
        self.button_video.clicked.connect(self.PredictVideo)

        self.button_pic = QPushButton('检测图片', self)
        self.button_pic.setGeometry(100, 200, 200, 50)
        self.button_pic.clicked.connect(self.PredictPic)

    def PredictVideo(self):
        # 更换文件路径为你想要执行的Python文件路径
        python_file_path = 'predict_video.py.py'
        subprocess.Popen(['python', python_file_path])


    def PredictPic(self):
        # 更换文件路径为你想要执行的Python文件路径
        python_file_path = 'predict_pic.py'
        subprocess.Popen(['python', python_file_path])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ButtonClickApp()
    ex.show()
    sys.exit(app.exec_())
