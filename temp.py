self.pushButton_2.clicked.connect(self.registration, 2)
        self.pushButton_3.clicked.connect(self.registration, 3)
        self.pushButton_4.clicked.connect(self.registration, 4)
        self.pushButton_5.clicked.connect(self.registration, 5)
        self.pushButton_6.clicked.connect(self.registration, 6)
        self.pushButton_7.clicked.connect(self.registration, 7)
        self.pushButton_8.clicked.connect(self.registration, 8)
        self.pushButton_9.clicked.connect(self.registration, 9)
        self.pushButton_10.clicked.connect(self.registration, 10)
        self.pushButton_11.clicked.connect(self.registration, 11)
        self.pushButton_12.clicked.connect(self.registration, 12)




def registration(self, place):
        cur = self.con.cursor()
        cur.execute("""UPDATE tbl SET freeornor = '1' WHERE numberoftable = '1'""")
        self.con.commit()


    def reg1(self, place):
        cur = self.con.cursor()
        cur.execute("""UPDATE tbl SET freeornor = '1' WHERE numberoftable = '1'""")
        self.con.commit()



def reg2(self):
        cur = self.con.cursor()
        cur.execute("""UPDATE tbl SET freeornor = '1' WHERE numberoftable = '2'""")
        self.con.commit()

    def reg3(self):
        cur = self.con.cursor()
        cur.execute("""UPDATE tbl SET freeornor = '1' WHERE numberoftable = '3'""")
        self.con.commit()

    def reg4(self):
        cur = self.con.cursor()
        cur.execute("""UPDATE tbl SET freeornor = '1' WHERE numberoftable = '4'""")
        self.con.commit()

    def reg5(self):
        cur = self.con.cursor()
        cur.execute("""UPDATE tbl SET freeornor = '1' WHERE numberoftable = '5'""")
        self.con.commit()
    
    def reg6(self):
        cur = self.con.cursor()
        cur.execute("""UPDATE tbl SET freeornor = '1' WHERE numberoftable = '6'""")
        self.con.commit()

    def reg7(self):
        cur = self.con.cursor()
        cur.execute("""UPDATE tbl SET freeornor = '1' WHERE numberoftable = '7'""")
        self.con.commit()

    def reg8(self):
        cur = self.con.cursor()
        cur.execute("""UPDATE tbl SET freeornor = '1' WHERE numberoftable = '8'""")
        self.con.commit()

    def reg9(self):
        cur = self.con.cursor()
        cur.execute("""UPDATE tbl SET freeornor = '1' WHERE numberoftable = '9'""")
        self.con.commit()
    
    def reg10(self):
        cur = self.con.cursor()
        cur.execute("""UPDATE tbl SET freeornor = '1' WHERE numberoftable = '10'""")
        self.con.commit()

    def reg11(self):
        cur = self.con.cursor()
        cur.execute("""UPDATE tbl SET freeornor = '1' WHERE numberoftable = '11'""")
        self.con.commit()

    def reg12(self):
        cur = self.con.cursor()
        cur.execute("""UPDATE tbl SET freeornor = '1' WHERE numberoftable = '12'""")
        self.con.commit()