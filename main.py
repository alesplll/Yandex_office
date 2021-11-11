import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('app.ui', self)  # Загружаем дизайн
        self.con = sqlite3.connect("appdb.sqlite")
        self.pushButton_2.clicked.connect(self.reg1)

    def reg1(self):
        cur = self.con.cursor()
        cur.execute("""UPDATE tbl SET freeornor = '1' WHERE numberoftable = '2'""")
        self.con.commit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())