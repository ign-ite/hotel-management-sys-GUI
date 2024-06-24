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
        root = Tk()
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        font10 = "-family {Segoe UI} -size 17 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 28 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 23 -weight bold -slant roman" \
                " -underline 0 -overstrike 0"

        root.geometry("881x582+249+104")
        root.title("HOTEL MANAGEMENT")
        root.configure(background="#d9d9d9")

        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.94)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=825)

        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.04, rely=0.46, relheight=0.48, relwidth=0.93)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=764)
        self.Text1.configure(wrap=WORD)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.12, rely=0.15, height=48, width=377)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''ENTER THE ROOM NO.   :''')