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
                try:
                    while True:
                        s = pickle.load(f)
                        if s.room_no == v:
                            n = 1
                            name1 = s.name

                            print(" ")
                        else:
                            pickle.dump(s, f1)
                except EOFError:
                    if n == 0:
                        self.Text1.insert(INSERT, "NO GUEST FOUND""\n")

                    elif n == 1:

                        self.Text1.insert(INSERT, "THANK YOU  " + name1.upper() + " FOR VISTING US""\n")
                    pass
                f.close()
                f1.close()
                os.remove("hotel.dat")
                os.rename("hote.dat", "hotel.dat")

            else:
                self.Text1.insert(INSERT, "invalid input please input a valid ROOM NO.""\n")

        root = Tk()

        _bgcolor = '#ffffff'  # X11 color: 'white'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff'  # X11 color: 'white'
        _ana1color = '#ffffff'  # X11 color: 'white'
        _ana2color = '#ffffff'  # X11 color: 'white'
        font10 = "-family {Courier New} -size 10 -weight normal -slant" \
                 " roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 23 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 24 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant " \
                "roman -underline 0 -overstrike 0"

        root.geometry("1011x750")
        root.title("HOTEL MANAGEMENT")
        root.configure(background="#ffffff")
        root.configure(highlightbackground="#ffffff")
        root.configure(highlightcolor="black")
