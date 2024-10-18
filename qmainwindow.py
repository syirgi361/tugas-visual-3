from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow

app = QApplication([])

Window = QMainWindow ()
label = QLabel(Window)
label.setText("LABEL1")
label.move(200,0)

button = QPushButton(Window)
button.setText("BUTTON!")

Window.show()
app.exec_()