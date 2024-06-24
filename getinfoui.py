import os
import pickle

details_list=[]
l2=[]
G = []
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
    restart_program()

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

class save:
    def __init__(self, NAME_PRO, ADDRESS_PRO, MOBILE_NO_PRO, ROOM_NO_PRO, PRICE_PRO):
        self.name=NAME_PRO
        self.address=ADDRESS_PRO
        self.mobile_no=MOBILE_NO_PRO
        self.room_no=ROOM_NO_PRO
        self.price=PRICE_PRO
        print(self.name,self.address,self.mobile_no,self.room_no,self.price)

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


class HOTEL_MANAGEMENT:
    def __init__(self):
        def gotinfo():
            self.gettininfo = str(self.gather.get())
            print(self.gettininfo)
            print("\n")
            if self.gettininfo.isdigit() == True and len(self.gettininfo) != 0:
                self.Text1.insert(INSERT, " valid room number ""\n")
            else :
                self.Text1.insert(INSERT,"invalid room number""\n")

            try:
                n = 0
                f2 = open("hotel.dat", "rb")
                while True:
                    s = pickle.load(f2)
                    a = str(s.room_no)
                    print (a)
                    if self.gettininfo == a:
                        n = 1
                        print("NAME-", "\t", "\t", s.name)
                        print("\n")
                        print("ADDRESS-", "\t", s.address)
                        print("\n")
                        print("MOBILE NO.-", "  ", s.mobile_no)
                        print("\n")
                        print("HIS TOTAL BILL IS Rs.", s.price)
                    elif EOFError:
                        if n == 0:
                            print("NO GUEST IN ROOM ", self.gettininfo)
                        else:
                            n = 0
                            continue
            except EOFError:
                pass
                f2.close()
