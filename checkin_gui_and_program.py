import os
import pickle
import sys
import os
from subprocess import call

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
details_list=[]


def file_save():
    NAME_PRO = details_list[0]
    ADDRESS_PRO = details_list[1]
    MOBILE_NO_PRO = details_list[2]
    ROOM_NO_PRO = details_list[3]
    PRICE_PRO = details_list[4]
    f = open("hotel.dat", "ab")
    a=save(NAME_PRO,ADDRESS_PRO,MOBILE_NO_PRO,ROOM_NO_PRO,PRICE_PRO)
    pickle.dump(a,f,protocol=2)
    f.close()
    listq=[str(NAME_PRO),str(ADDRESS_PRO),str(MOBILE_NO_PRO),str(ROOM_NO_PRO),str(PRICE_PRO)]
    myVars = {'A':NAME_PRO,"B":ADDRESS_PRO,"C":MOBILE_NO_PRO,"D":ROOM_NO_PRO,"E":PRICE_PRO }

    fo=open("recipt.txt","w+")
    for h in range(0,5):
        fo.write(listq[h]+"\r\n")
    fo.close()
    call(["python", "recipt.py"])
    restart_program()

u = list()
Delux = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
Semi_Delux = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)
General = (26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45)
Joint_Room = (46, 47, 48, 49, 50, 46, 47, 48, 49, 50)
m = [9]
G = []
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


class save:
    def __init__(self, NAME_PRO, ADDRESS_PRO, MOBILE_NO_PRO, ROOM_NO_PRO, PRICE_PRO):
        self.name = NAME_PRO
        self.address = ADDRESS_PRO
        self.mobile_no = MOBILE_NO_PRO
        self.room_no = ROOM_NO_PRO
        self.price = PRICE_PRO


class HOTEL_MANGMENT_checkin:

    def __init__(self):
        self.NAME = ""
        self.ADDERESS = ""
        self.MOBILE = ""
        self.DAYS = 0
        self.price = 0
        self.room = 0

        def chk_name():
            while True:

                self.k = str(self.name.get())

                a = self.k.isdigit()
                if len(self.k) != 0 and a != True:
                    self.NAME = self.k
                    self.Text1.insert(INSERT, "name has been inputed""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "invalid input please input a valid name""\n")

                    break

        def chk_add():
            while True:
                self.g = str(self.addr.get())

                ak = self.g.isdigit()
                if len(self.g) != 0 and ak != True:
                    self.ADDERESS = self.g
                    self.Text1.insert(INSERT, "address has been inputed""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "invalid input please input a valid address""\n")

                    break

        def chk_mo():
            while True:

                self.h = str(self.mobile.get())
                if self.h.isdigit() == True and len(self.h) != 0 and len(self.h) == 10:
                    self.MOBILE = self.h
                    self.Text1.insert(INSERT, "mobile number has been inputed""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "invalid input ""\n")
                    break

                def enter(self):
                    self.name = self.NAME
                    self.address = self.ADDERESS
                    self.mobile_no = self.MOBILE
                    self.no_of_days = int(self.DAYS)

                def tor(self):

                    if self.ch == 1:
                        self.price = self.price + (2000 * self.no_of_days)
                        m[0] = 1
                    elif self.ch == 2:
                        self.price = self.price + (1500 * self.no_of_days)
                        m[0] = 2
                    elif self.ch == 3:
                        self.price = self.price + (1000 * self.no_of_days)
                        m[0] = 3
                    elif self.ch == 4:
                        self.price = self.price + (1700 * self.no_of_days)
                        m[0] = 4

                def payment_option(self):
                    op = self.p
                    if op == 1:
                        self.Text1.insert(INSERT, "no discount""\n")
                    elif op == 2:
                        self.price = self.price - ((self.price * 10) / 100)
                        self.Text1.insert(INSERT, "10% discount""\n")

                def bill(self):

                    if m[0] == 1:
                        a = Delux
                    elif m[0] == 2:
                        a = Semi_Delux
                    elif m[0] == 3:
                        a = General
                    elif m[0] == 4:
                        a = Joint_Room

                    G = []
                    f2 = open("hotel.dat", "rb")
                    try:
                        while True:
                            s = pickle.load(f2)

                            k = s.room_no
                            G.append(k)
                            continue

                    except EOFError:
                        pass

                    for r in a:
                        if r not in G:
                            self.room = r
                            break
                        else:
                            continue
                    self.room = r
                    f2.close()

                    details_list.append(self.name)
                    details_list.append(self.address)
                    details_list.append(self.mobile_no)
                    details_list.append(self.room)
                    details_list.append(self.price)

                    file_save()