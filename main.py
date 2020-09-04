import csv
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.title = "The Price"
        self.left = 100
        self.top = 150
        self.width = 640
        self.height = 480
        self.setStyleSheet("background-color: rgba(170, 255, 255, 1)")
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.initUI()
        self.show()

    def initUI(self):
        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setStyleSheet("QPushButton {margin:1px; padding: 3px; border: 1px solid gray; "
                                   "border-radius: 20px;background-color: rgba(200, 255, 255, 1); "
                                   "border-width: 2px;}"
                                   "QPushButton:hover:!pressed {background-color: rgba(255, 255, 255, 1)}")
        self.button1.setGeometry(100, 200, 200, 80)
        self.button1.setText("Check Price")
        self.button1.setFont(QtGui.QFont('Arial', 15))
        self.button1.clicked.connect(lambda: self.first_clicked('check'))

        self.button2 = QtWidgets.QPushButton(self)
        self.button2.setStyleSheet("QPushButton {margin:1px; padding: 3px; border: 1px solid gray; "
                                   "border-radius: 20px;background-color: rgba(200, 255, 255, 1); "
                                   "border-width: 2px;}"
                                   "QPushButton:hover:!pressed {background-color: rgba(255, 255, 255, 1)}")
        self.button2.setGeometry(340, 200, 200, 80)
        self.button2.setText("Add Price")
        self.button2.setFont(QtGui.QFont('Arial', 15))
        self.button2.clicked.connect(lambda: self.first_clicked('add'))

    def first_clicked(self, which):
        self.button1.deleteLater()
        self.button2.deleteLater()

        if which == 'check':
            self.check_price_window()
        if which == 'add':
            self.add_price_window()

        def back_clicked():
            ex.close()
            self.__init__()

        back_button = QtWidgets.QPushButton(self)
        back_button.setText("← Back")
        back_button.setGeometry(1, 1, 100, 45)
        back_button.setFont(QtGui.QFont('Times New Roman', 10))
        back_button.setStyleSheet("QPushButton {margin:1px; padding: 2px; border: 1px solid gray; "
                                  "border-radius: 20px;background-color: rgba(200, 255, 255, 1); "
                                  "border-width: 2px;}"
                                  "QPushButton:hover:!pressed {background-color: rgba(255, 255, 255, 1)}")
        back_button.clicked.connect(back_clicked)
        back_button.show()

    def check_price_window(self):
        check_combo = QtWidgets.QComboBox(self)
        check_combo.setGeometry(50, 150, 420, 50)
        check_combo.setStyleSheet("QComboBox {border: 1px solid gray;border-radius: 10px;padding-left: 15px; "
                                  "background-color: rgba(200, 255,255, 1); font: 25px;} "
                                  "QComboBox:drop-down:!pressed {border: 1px border-radius: 20px;border: 1px solid "
                                  "gray; padding: 1px;}")
        check_combo.setFont(QtGui.QFont('Times New Roman', 15))
        check_combo.setEditable(False)

        submit_button = QtWidgets.QPushButton(self)
        submit_button.setGeometry(485, 150, 125, 50)
        submit_button.setStyleSheet("QPushButton {margin:1px; padding: 3px; border: 1px solid gray; "
                                    "border-radius: 20px;background-color: rgba(200, 255, 255, 1); "
                                    "border-width: 2px;}"
                                    "QPushButton:hover:!pressed {background-color: rgba(255, 255, 255, 1)}")
        submit_button.setText("Check")
        submit_button.setFont(QtGui.QFont('Times New Roman', 15))

        price_label = QtWidgets.QLabel(self)
        price_label.setGeometry(230, 240, 200, 50)
        price_label.setFont(QtGui.QFont("Times New Roman", 15))

        with open('data.csv') as data:
            reader = enumerate(csv.reader(data))
            items_list = []
            for i, row in reader:
                if i > 0:
                    item_name = row[0]
                    item_price = row[1]
                    items_list.append([item_name, item_price])

        names = [u[0] for u in items_list]
        names.sort()
        check_combo.addItems(names)
        check_combo.show()
        submit_button.show()

        def submit_clicked():
            item_to_check = check_combo.currentText()
            for item in items_list:
                if item[0] == item_to_check:
                    price_label.setText(f"Price: ₵ {item[1]}")
                    price_label.setStyleSheet("QLabel {margin:1px; padding: 3px; border: 1px solid gray; "
                                              "border-radius: 20px;background-color: rgba(200, 255, 255, 1); "
                                              "border-width: 2px;}")
                    price_label.adjustSize()

        submit_button.clicked.connect(submit_clicked)

        price_label.show()

    def add_price_window(self):
        take_name = QtWidgets.QLineEdit(self)
        take_name.setGeometry(50, 150, 420, 50)
        take_name.setFont(QtGui.QFont('Times New Roman', 15))
        take_name.setPlaceholderText("Name")
        take_name.setStyleSheet("QLineEdit {border: 1px solid gray;border-radius: 10px;padding-left: 15px; "
                                "background-color: rgba(200, 255,255, 1); font: 25px;}"
                                "QLineEdit:focus {background-color: rgba(255, 255, 255, 1)}")

        take_price = QtWidgets.QLineEdit(self)
        take_price.setGeometry(485, 150, 125, 50)
        take_price.setFont(QtGui.QFont('Times New Roman', 15))
        take_price.setPlaceholderText("Price")
        take_price.setStyleSheet("QLineEdit {border: 1px solid gray;border-radius: 10px;padding-left: 15px; "
                                 "background-color: rgba(200, 255,255, 1); font: 25px;}"
                                 "QLineEdit:focus {background-color: rgba(255, 255, 255, 1)}")

        save_button = QtWidgets.QPushButton(self)
        save_button.setGeometry(270, 240, 125, 50)
        save_button.setFont(QtGui.QFont('Times New Roman', 15))
        save_button.setText("Save")
        save_button.setStyleSheet("QPushButton {margin:1px; padding: 3px; border: 1px solid gray; "
                                  "border-radius: 20px;background-color: rgba(200, 255, 255, 1); "
                                  "border-width: 2px;}"
                                  "QPushButton:hover:!pressed {background-color: rgba(255, 255, 255, 1)}")

        take_name.show()
        take_price.show()
        save_button.show()

        def save_clicked():
            name_to_add = take_name.text()
            price_to_add = take_price.text()

            message_box = QtWidgets.QMessageBox(self)
            message_box.setDefaultButton(QMessageBox.Ok)
            message_box.setStyleSheet(
                "QMessageBox {border: 1px solid gray;border-radius: 10px;padding-left: 15px; "
                "background-color: rgba(125, 255,255, 1); font: 25px;}"
                "QPushButton {font-size: 20px; background-color: rgba(200, 255,255, 1); border-radius: "
                "10px; border: 1px solid gray; padding-left: 20px; padding-right: 20px; padding-top: 5px;"
                "padding-bottom: 5px;} "
                "QPushButton:hover:!pressed {background-color: rgba(255, 255, 255, 1)}"
                "QLabel {background-color: rgba(125, 255,255, 1); font: 25px;}")

            if name_to_add and price_to_add:
                with open('data.csv', 'wa', newline='') as data_file:
                    writer = csv.writer(data_file)
                    writer.writerow([str(name_to_add), str(price_to_add)])

                    message_box.setIcon(QMessageBox.Information)
                    message_box.setWindowTitle("Success")
                    message_box.setText("Item and Price added Successfully!")
                    message_box.setInformativeText(f"Item name: {name_to_add}\nItem Price: ₵ {price_to_add}")
                    message_box.show()
            else:
                message_box.setIcon(QMessageBox.Critical)
                message_box.setWindowTitle("Error")
                message_box.setText("Price or Name not inputted")
                message_box.show()

        save_button.clicked.connect(save_clicked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
