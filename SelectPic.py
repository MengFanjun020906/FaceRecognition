import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog

def pick_file():
    app = QApplication(sys.argv)
    window = FilePicker()
    window.show()
    app.exec_()  # 执行Qt应用程序的事件循环
    return window.selected_file  # 返回选定的文件路径

class FilePicker(QWidget):
    def __init__(self):
        super().__init__()
        self.selected_file = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('File Picker')
        self.setGeometry(100, 100, 300, 200)

        self.pick_button = QPushButton('选择文件', self)
        self.pick_button.setGeometry(100, 100, 100, 30)
        self.pick_button.clicked.connect(self.pickFile)

        self.pick_button2 = QPushButton('关闭', self)
        self.pick_button2.setGeometry(100, 200, 100, 30)
        self.pick_button2.clicked.connect(self.close())

    def pickFile(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "All Files (*)", options=options)
        if file_name:
            # 设置选定的文件路径
            self.selected_file = file_name
            self.close()  # 关闭窗口

if __name__ == '__main__':
    file_path = pick_file()
    print("选择的文件路径为:", file_path)
