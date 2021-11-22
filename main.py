import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        inf = ''
        uic.loadUi('main.ui', self)
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        info = cur.execute("SELECT * FROM coffee")
        for i in info:
            inf += str(list(i)[1:-1])
        con.close()
        self.label.setText(inf)


class Test:
    def __init__(self):
        con = sqlite3.connect("exam.db")
        cur = con.cursor()

        block_columns = [f"'{i}'" for i in self.count_questions]
        block_names = [f"{self.count_questions[i]}" for i in self.count_questions]

        names_columns = f"name, {', '.join(block_columns)}, flag_time, time, last_number"
        value_columns = f"'{self.name}', {', '.join(block_names)}, {self.flag_time}, '{self.time}', 1"
        cor.execute("""UPDATE films SET duration = 42 WHERE NOT duration""")

        cur.execute(f"""INSERT INTO Tests({names_columns}) VALUES({value_columns})""")
        con.commit()
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Coffee()
    window.show()
    app.exec_()