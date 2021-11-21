import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        info = cur.execute("SELECT * FROM coffee")
        inf = ''
        for i in info:
            inf += str(list(i)[1:-1])
        con.close()
        self.label.setText(inf)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Coffee()
    window.show()
    app.exec_()