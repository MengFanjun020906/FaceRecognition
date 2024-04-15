import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
from predict import Retinaface  # 假设这是人脸检测的函数

class CameraApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        # 初始化摄像头
        self.camera = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateFrame)
        self.timer.start(100)

    def initUI(self):
        self.setWindowTitle('Camera App')
        self.setGeometry(100, 100, 640, 480)

        self.label = QLabel(self)
        self.label.setFixedSize(640, 480)

        self.button = QPushButton('检测人脸', self)
        self.button.clicked.connect(self.Retinaface)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def updateFrame(self):
        ret, frame = self.camera.read()
        if ret:
            # 将图像转换为RGB格式
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # 将RGB图像转换为Qt格式
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

            # 显示图像
            pixmap = QPixmap.fromImage(qt_image)
            self.label.setPixmap(pixmap)

    def detectFace(self):
        # 执行人脸检测并获取结果
        faces = Retinaface()

        # 在图像上绘制检测到的人脸
        frame = self.camera.read()[1]
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 更新显示
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_image)
        self.label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CameraApp()
    ex.show()
    sys.exit(app.exec_())
