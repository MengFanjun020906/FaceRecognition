from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QMainWindow, QMessageBox

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
        self.pick_button2.clicked.connect(QApplication.quit)
