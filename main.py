import sys
import sqlite3

from functools import partial
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('app.ui', self)  # Загружаем дизайн
        self.con = sqlite3.connect("appdb.sqlite")

        A = []
        A.append(self.pushButton_1.clicked.connect(partial(self.reg1, 1)))
        A.append(self.pushButton_2.clicked.connect(partial(self.reg1, 2)))
        A.append(self.pushButton_3.clicked.connect(partial(self.reg1, 3)))
        A.append(self.pushButton_4.clicked.connect(partial(self.reg1, 4)))
        A.append(self.pushButton_5.clicked.connect(partial(self.reg1, 5)))
        A.append(self.pushButton_6.clicked.connect(partial(self.reg1, 6)))
        A.append(self.pushButton_7.clicked.connect(partial(self.reg1, 7)))
        A.append(self.pushButton_8.clicked.connect(partial(self.reg1, 8)))
        A.append(self.pushButton_9.clicked.connect(partial(self.reg1, 9)))
        A.append(self.pushButton_10.clicked.connect(partial(self.reg1, 10)))
        A.append(self.pushButton_11.clicked.connect(partial(self.reg1, 11)))
        A.append(self.pushButton_12.clicked.connect(partial(self.reg1, 12)))

        self.upd()

    def reg1(self, place):
        self.pushButton_confirm.clicked.connect(partial(self.hire, place))
        #не шарю че сделать, нужно условие чтобы по нажатию на конфирм срабатлывало hire()
    
    def hire(self, place):
        sender = self.sender()
        print(sender.text())
        #print(place)
        cur.execute(f"""SELECT {i} FROM tbl;""")
        temp = cur.fetchone()
        if temp == 1:
            temp = 0
        else:
            temp = 1
        cur = self.con.cursor()
        cur.execute(f"""UPDATE tbl SET freeornor = {temp} WHERE numberoftable = {place} """)
        self.con.commit()



    def upd(self):
        global A
        cur = self.con.cursor()
        for i in range(12):
            cur.execute(f"""SELECT {i} FROM tbl;""")
            YorN = cur.fetchone()
            if YorN == 1:
                A[i].setEnabled(False)
            else:
                A[i].setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())