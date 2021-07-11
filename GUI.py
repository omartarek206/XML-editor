from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class win(QMainWindow)
    def __init__




def clicked():
    print("tam elda3s")
def window():
    app= QApplication(sys.argv)
    win= QMainWindow()
    win.setGeometry(200,200,500,500)
    win.setWindowTitle("Simple GUI")
    label = QtWidgets.QLabel(win)
    label.setText("label")
    label.move(50,50)

    b1= QtWidgets.QPushButton(win)
    b1.setText("ed3as")
    b1.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec())

window()