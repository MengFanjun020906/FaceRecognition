import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Output Window Example")
        self.setGeometry(100, 100, 600, 400)

        self.output_text_edit = QPlainTextEdit()
        self.output_text_edit.setReadOnly(True)  # 设置为只读模式

        layout = QVBoxLayout()
        layout.addWidget(self.output_text_edit)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 在初始化期间添加示例输出信息
        self.showOutput()

    def showOutput(self):
        # 这里模拟输出信息
        for i in range(10):
            self.output_text_edit.appendPlainText(f"Output message {i}")

        self.output_text_edit.verticalScrollBar().setValue(self.output_text_edit.verticalScrollBar().maximum())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
