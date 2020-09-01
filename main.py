import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.title = "The Price"
        self.left = 35
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setGeometry(100, 200, 200, 80)
        self.button1.setText("Check Price")
        self.button1.setFont(QtGui.QFont('Arial', 15))
        self.button1.clicked.connect(lambda: self.first_clicked('check'))

        self.button2 = QtWidgets.QPushButton(self)
        self.button2.setGeometry(340, 200, 200, 80)
        self.button2.setText("Add Price")
        self.button2.setFont(QtGui.QFont('Arial', 15))
        self.button2.clicked.connect(lambda: self.first_clicked('add'))

        self.show()

    def first_clicked(self, which):
        if which == 'check':
            print('check')
        if which == 'add':
            print('add')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
