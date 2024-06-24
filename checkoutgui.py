import os
import pickle
import sys

details_list = []
l2 = []
G = []


def file_save():
    NAME_PRO = details_list[0]
    ADDRESS_PRO = details_list[1]
    MOBILE_NO_PRO = details_list[2]
    ROOM_NO_PRO = details_list[3]
    PRICE_PRO = details_list[4]
    f = open("hotel.dat", "ab")
    a = save(NAME_PRO, ADDRESS_PRO, MOBILE_NO_PRO, ROOM_NO_PRO, PRICE_PRO)
    pickle.dump(a, f, protocol=2)
    f.close()
    restart_program()


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
        print(self.name, self.address, self.mobile_no, self.room_no, self.price)


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


class New_Toplevel:

    def __init__(self):
        def check_room():
            self.rom = str(self.data.get())
            print(self.rom)
            print("\n")
            if self.rom.isdigit() == True and len(self.rom) != 0:
                self.Text1.insert(INSERT, " valid room number ""\n")
                v = int(self.rom)
                f = open("hotel.dat", "rb")
                f1 = open("hote.dat", "ab")
                n = 0
