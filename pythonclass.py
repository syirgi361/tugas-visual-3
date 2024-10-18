from PyQt5.QtWidgets import QMainWindow,QWidget,QApplication,QPushButton,QLabel

class MyWindow(QMainWindow):
    def _init_(self):
        super().__init__()
        self.label = QLabel(self)
        self.label.setText("LABEL1")
        self.label.move(200,50)
        self.button= QPushButton (self)
        self.button.setText("BUTTON1")

        app = QApplication([])
        window = MyWindow()
        window.show()
        app.exec_()