import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.pushButton.clicked.connect(self.chang)

    def chang(self):
        con = sqlite3.connect("cofe.db")
        cur = con.cursor()
        if self.lineEdit.text() != '':
            a = self.lineEdit.text().split()
            if len(a) == 6:
                a = f"'{a[0]}', '{a[1]}', '{a[2]}', '{a[3]}', '{a[4]}', '{a[5]}'"
                cur.execute(f"""INSERT INTO coffee(variety, roasting, condition, taste, price, volume)
                                VALUES({a})""")
        if self.lineEdit1.text() != '' and self.lineEdit2.text() != '':
            a, b = self.lineEdit1.text().split(), self.lineEdit2.text()
            if len(a) == 2:
                a1, a2 = a[0], a[1]
                cur.execute(f"""UPDATE coffee SET {a1} = {b} WHERE id = {a2}""")
        con.commit()
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Coffee()
    window.show()
    app.exec_()