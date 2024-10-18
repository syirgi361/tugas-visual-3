from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton,QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.label . setText("LABEL1")
        self.label .move(200.50)
        self.button = QPushButton(self)
        self.button.setText("BUTTON1")
        self.setGeometry(0,0,400,400)
        self.setWindowTitle("Belajar PyQt5")

        app = QApplication ([])
        window = MyWindow()
        app.exec_()