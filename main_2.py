import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        if self.textEdit.setText() != '':
            a = self.textEdit.setText()
        #cor.execute("""UPDATE films SET duration = 42 WHERE NOT duration""")

        cur.execute(f"""INSERT INTO coffee('variety, roasting, condition, taste, price, volume') VALUES({a})""")
        con.commit()
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Coffee()
    window.show()
    app.exec_()