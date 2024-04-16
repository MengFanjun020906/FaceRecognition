from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtMultimedia import *
import untitled

class mywindow(QtWidgets.QMainWindow,untitled.Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

        # 创建摄像头实例
        self.camer = QCamera()

        # 设置摄像头的捕获模式
        # 拍照模式 QCamera.CaptureMode.CaptureStillImage
        # 取景器模式 QCamera.CaptureMode.CaptureViewfinder
        # 视频录制模式 QCamera.CaptureMode.CaptureVideo
        self.camer.setCaptureMode(QCamera.CaptureMode.CaptureStillImage)

        # 将摄像头实例放入相对应的组件中
        self.camer.setViewfinder(self.widget)

        # 创建一个用于摄像头拍照的类
        self.capture = QCameraImageCapture(self.camer)

        # 开启摄像机

        #self.camer.start()

        # 给保存并拍照按钮绑定函数
        self.save_pic.clicked.connect(self.save_img)
        self.save_pic.clicked.connect(self.current_show)
        self.click = 1

        # 给截图显示按钮绑定函数
        self.screenshot.clicked.connect(lambda: self.camer.start())

    def save_img(self):

        # 拍摄图片
        self.capture.capture()
        # 把拍摄的图像保存到缓存
        self.capture.setCaptureDestination(QCameraImageCapture.CaptureDestination.CaptureToBuffer)
        # 如果成功保存到缓存，会自动发送一个imageCapture信号
        self.capture.imageCaptured.connect(self.message_save)
        self.click += 1

    def message_save(self,id,img:QtGui.QImage):
        print(id)
        print(img)
        img.save(f'{self.click-1}.png')
        self.capture.imageCaptured.disconnect(self.message_save)

    def current_show(self):
        # 拍摄图片
        self.capture.capture()
        # 把拍摄的图像保存到缓存
        self.capture.setCaptureDestination(QCameraImageCapture.CaptureDestination.CaptureToBuffer)
        # 如果成功保存到缓存，会自动发送一个imageCapture信号
        self.capture.imageCaptured.connect(self.message_show)


    def message_show(self, id, img: QtGui.QImage):
        scalimg = img.scaled(self.label.width(),self.label.height(),QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.label.setPixmap(QtGui.QPixmap.fromImage(scalimg))
        self.capture.imageCaptured.disconnect(self.message_show)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())