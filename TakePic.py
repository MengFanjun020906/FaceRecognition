
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QMessageBox
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtMultimedia import *
import sys
import TakePicUi

class mywindow(QtWidgets.QMainWindow,TakePicUi.Ui_MainWindow):


    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.saved_image = None
        # 创建摄像头实例
        self.camer = QCamera(QCameraInfo.availableCameras()[1])

        self.camer.setCaptureMode(QCamera.CaptureStillImage)

        # 将摄像头实例放入相对应的组件中
        self.camer.setViewfinder(self.widget)

        # 创建一个用于摄像头拍照的类
        self.capture = QCameraImageCapture(self.camer)

        self.btn_save.clicked.connect(self.save_img)

        #点击拍照按钮，拍下照片
        self.save_pic.clicked.connect(self.current_show)
        self.click = 1

        # 给截图显示按钮绑定函数
        #self.camer = QCamera(0)
        self.screenshot.clicked.connect(lambda: self.camer.start())

    def save_img(self):

        text = self.text_edit.text()

        # 拍摄图片
        if self.saved_image and text:
            file_path = f"face_dataset/{text}.jpg"
            # file_path += f"{text}.jpg"
            self.saved_image.save(file_path)

            QMessageBox.information(self,"保存成功","图片已保存")
        elif not self.saved_image or not text:
            QMessageBox.warning(self, "无文本内容", "文本框中无内容，无法保存")
        else:
            QMessageBox.critical(self, "保存失败,保存图片出现错误")

    def message_save(self,id,img:QtGui.QImage):
        print(id)
        print(img)
        self.saved_image = img
        img.save(f'{self.click-1}.jpg')

        self.capture.imageCaptured.disconnect(self.message_save)

    def current_show(self):
        # 在拍摄图片前连接信号和槽函数
        self.capture.imageCaptured.connect(self.message_show)


        # 拍摄图片
        self.capture.capture()

        # 把拍摄的图像保存到缓存
        self.capture.setCaptureDestination(QCameraImageCapture.CaptureToBuffer)

    def message_show(self, id, img: QtGui.QImage):
        self.saved_image = img
        scalimg = img.scaled(self.label.width(),self.label.height(),QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.label.setPixmap(QtGui.QPixmap.fromImage(scalimg))

        # 拍摄完成后断开信号和槽函数的连接
        self.capture.imageCaptured.disconnect(self.message_show)

    def closeEvent(self, event):
        # 关闭窗口时停止摄像头
        self.camer.stop()
        event.accept()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())
