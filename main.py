import sys
import sqlite3

from functools import partial
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractButton, QMessageBox
A = []
date = 16

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pp.ui', self)  # Загружаем дизайн
        self.con = sqlite3.connect("ppdb.sqlite")
        
        self.pushButton_1.clicked.connect(partial(self.reg1, 1))
        self.pushButton_2.clicked.connect(partial(self.reg1, 2))
        self.pushButton_3.clicked.connect(partial(self.reg1, 3))
        self.pushButton_4.clicked.connect(partial(self.reg1, 4))
        self.pushButton_5.clicked.connect(partial(self.reg1, 5))
        self.pushButton_6.clicked.connect(partial(self.reg1, 6))
        self.pushButton_7.clicked.connect(partial(self.reg1, 7))
        self.pushButton_8.clicked.connect(partial(self.reg1, 8))
        self.pushButton_9.clicked.connect(partial(self.reg1, 9))
        self.pushButton_10.clicked.connect(partial(self.reg1, 10))
        self.pushButton_11.clicked.connect(partial(self.reg1, 11))
        self.pushButton_12.clicked.connect(partial(self.reg1, 12))
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Error")
        self.msg.setText("Time doesn't exist")
        A.append(self.pushButton_1)
        A.append(self.pushButton_2)
        A.append(self.pushButton_3)
        A.append(self.pushButton_4)
        A.append(self.pushButton_5)
        A.append(self.pushButton_6)
        A.append(self.pushButton_7)
        A.append(self.pushButton_8)
        A.append(self.pushButton_9)
        A.append(self.pushButton_10)
        A.append(self.pushButton_11)
        A.append(self.pushButton_12)
        self.upd()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.upd)
        self.timer.start(500)

    def keyPressEvent(self, event):
        if event.key() == 16777220:
            self.confirmed()
        event.accept()


    def reg1(self, place):
        pass

    def day(self):
        dateselected = self.calendarWidget.selectedDate()
        return str(dateselected.toPyDate())[8:]


    def confirmed(self):
        if self.pushButton_1.isChecked() == True:
            place = 1
        elif self.pushButton_2.isChecked() == True:
            place = 2
        elif self.pushButton_3.isChecked() == True:
            place = 3
        elif self.pushButton_4.isChecked() == True:
            place = 4
        elif self.pushButton_5.isChecked() == True:
            place = 5
        elif self.pushButton_6.isChecked() == True:
            place = 6
        elif self.pushButton_7.isChecked() == True:
            place = 7
        elif self.pushButton_8.isChecked() == True:
            place = 8
        elif self.pushButton_9.isChecked() == True:
            place = 9
        elif self.pushButton_10.isChecked() == True:
            place = 10
        elif self.pushButton_11.isChecked() == True:
            place = 11
        elif self.pushButton_12.isChecked() == True:
            place = 12
        print(place)
        self.hire(place)
            #self.pushButton_confirm.clicked.connect(partial(self.hire, place))
        #не шарю че сделать, нужно условие чтобы по нажатию на конфирм срабатлывало hire()
    

    def hire(self, place):
        date = self.day()
        cur = self.con.cursor()
        cur.execute(f"""SELECT freeornor{date} FROM tbl WHERE numberoftable = {place}""")
        temp = cur.fetchone()[0]
        print(temp)
        if temp == 1:
            temp = 0
        else:
            temp = 1
        cur = self.con.cursor()
        cur.execute(f"""UPDATE tbl SET freeornor{date} = {temp} WHERE numberoftable = {place} """)

        cur = self.con.cursor()
        cur.execute(f"""SELECT freeornor{date} FROM tbl WHERE numberoftable = {place}""")
        print(cur.fetchone()[0])
        self.con.commit()
        self.upd()


    def upd(self):
        global A
        global date
        date = self.day()
        try:
            tt = "freeornor"
            cur = self.con.cursor()
            for i in range(0, 12):
                cur.execute(f"""SELECT freeornor{date} FROM tbl WHERE numberoftable = {i+1}""")
                YorN = cur.fetchone()[0]
                A[i]
                if YorN == 1:
                    A[i].setText(f"{i+1} \n booked")
                else:
                    A[i].setText(f"{i+1}")
        except:
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.exec_()
            datt = QDate(2021, 12, 16)
            self.calendarWidget.setSelectedDate(datt)
            
            


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())