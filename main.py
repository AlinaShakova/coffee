import random
import sys
import sqlite3
from matplotlib import figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, \
    QWidget, QInputDialog, QTableWidgetItem


class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('menu_window.ui', self)


class Test:
    def __init__(self):
        self.flag_time = False
        self.time = ''
        self.name = ''
        self.count_questions = {'count_block_1': 0, 'count_block_2': 0, 'count_block_3': 0,
                                'count_block_4': 0, 'count_block_5': 0, 'count_block_6': 0,
                                'count_block_7': 0, 'count_block_8': 0, 'count_block_9': 0,
                                'count_block_10': 0, 'count_block_11': 0}
        self.last_number = 1

    def save_test(self):
        con = sqlite3.connect("exam.db")
        cur = con.cursor()

        block_columns = [f"'{i}'" for i in self.count_questions]
        block_names = [f"{self.count_questions[i]}" for i in self.count_questions]

        names_columns = f"name, {', '.join(block_columns)}, flag_time, time, last_number"
        value_columns = f"'{self.name}', {', '.join(block_names)}, {self.flag_time}, '{self.time}', 1"

        cur.execute(f"""INSERT INTO Tests({names_columns}) VALUES({value_columns})""")
        con.commit()
        con.close()

    def import_test(self, name):
        con = sqlite3.connect("exam.db")
        cur = con.cursor()

        test_settings = cur.execute(f"""SELECT * FROM Tests WHERE name = '{name}'""").fetchall()[0]

        for i, block in enumerate(self.count_questions):
            self.count_questions[block] = test_settings[i + 2]

        self.flag_time = test_settings[-3]
        self.time = test_settings[-2]
        self.last_number = test_settings[-1]
        self.name = name


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
