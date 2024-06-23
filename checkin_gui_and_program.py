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

                def submit_clicked():
                    if self.var1.get() == 1 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 0 and self.var5.get() == 1 and self.var6.get() == 0:
                        self.ch = 1
                        self.p = 2

                        enter(self)
                        tor(self)
                        payment_option(self)
                        bill(self)


                    elif self.var1.get() == 1 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 0 and self.var5.get() == 0 and self.var6.get() == 1:
                        self.ch = 1
                        self.p = 1

                        enter(self)
                        tor(self)
                        payment_option(self)
                        bill(self)
                    elif self.var1.get() == 0 and self.var2.get() == 1 and self.var3.get() == 0 and self.var4.get() == 0 and self.var5.get() == 0 and self.var6.get() == 1:
                        self.ch = 2
                        self.p = 1

                        enter(self)
                        tor(self)
                        payment_option(self)
                        bill(self)
                    elif self.var1.get() == 0 and self.var2.get() == 1 and self.var3.get() == 0 and self.var4.get() == 0 and self.var5.get() == 1 and self.var6.get() == 0:
                        self.ch = 2
                        self.p = 2

                        enter(self)
                        tor(self)
                        payment_option(self)
                        bill(self)
                    elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 1 and self.var4.get() == 0 and self.var5.get() == 0 and self.var6.get() == 1:
                        self.ch = 3
                        self.p = 1

                        enter(self)
                        tor(self)
                        payment_option(self)
                        bill(self)
                    elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 1 and self.var4.get() == 0 and self.var5.get() == 1 and self.var6.get() == 0:
                        self.ch = 3
                        self.p = 2

                        enter(self)
                        tor(self)
                        payment_option(self)
                        bill(self)

                    elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 1 and self.var5.get() == 0 and self.var6.get() == 1:
                        self.ch = 4
                        self.p = 1

                        enter(self)
                        tor(self)
                        payment_option(self)
                        bill(self)
                    elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 1 and self.var5.get() == 1 and self.var6.get() == 0:
                        self.ch = 4
                        self.p = 2

                        enter(self)
                        tor(self)
                        payment_option(self)
                        bill(self)

                    else:
                        self.Text1.insert(INSERT, "invalid choice please input a valid choice""\n")

                root = Tk()

                '''This class configures and populates the toplevel window.
                   top is the toplevel containing window.'''
                _bgcolor = '#ffffff'  # X11 color: 'white'
                _fgcolor = '#000000'  # X11 color: 'black'
                _compcolor = '#ffffff'  # X11 color: 'white'
                _ana1color = '#ffffff'  # X11 color: 'white'
                _ana2color = '#ffffff'  # X11 color: 'white'
                font10 = "-family {Courier New} -size 10 -weight normal -slant" \
                         " roman -underline 0 -overstrike 0"
                font11 = "-family {Segoe UI} -size 30 -weight bold -slant " \
                         "roman -underline 0 -overstrike 0"
                font12 = "-family {Segoe UI} -size 18 -weight bold -slant " \
                         "roman -underline 0 -overstrike 0"
                font13 = "-family {Segoe UI} -size 17 -weight bold -slant " \
                         "roman -underline 0 -overstrike 0"
                font14 = "-family {Segoe UI} -size 16 -weight bold -slant " \
                         "roman -underline 0 -overstrike 0"
                font15 = "-family {Segoe UI} -size 19 -weight bold -slant " \
                         "roman -underline 0 -overstrike 0"
                font16 = "-family {Segoe UI} -size 15 -weight bold -slant " \
                         "roman -underline 0 -overstrike 0"
                font9 = "-family {Segoe UI} -size 9 -weight normal -slant " \
                        "roman -underline 0 -overstrike 0"

                root.geometry("1069x742")
                root.title("HOTEL MANGMENT")
                root.configure(background="#ffffff")
                root.configure(highlightbackground="#ffffff")
                root.configure(highlightcolor="black")

                self.Text1 = Text(root)
                self.Text1.place(relx=0.03, rely=0.65, relheight=0.29, relwidth=0.93)
                self.Text1.configure(background="white")
                self.Text1.configure(font=font9)
                self.Text1.configure(foreground="black")
                self.Text1.configure(highlightbackground="#ffffff")
                self.Text1.configure(highlightcolor="black")
                self.Text1.configure(insertbackground="black")
                self.Text1.configure(selectbackground="#e6e6e6")
                self.Text1.configure(selectforeground="black")
                self.Text1.configure(width=994)
                self.Text1.configure(wrap=WORD)

                self.Frame1 = Frame(root)
                self.Frame1.place(relx=0.03, rely=0.05, relheight=0.12, relwidth=0.93)
                self.Frame1.configure(relief=GROOVE)
                self.Frame1.configure(borderwidth="2")
                self.Frame1.configure(relief=GROOVE)
                self.Frame1.configure(background="#ffffff")
                self.Frame1.configure(highlightbackground="#ffffff")
                self.Frame1.configure(highlightcolor="black")
                self.Frame1.configure(width=995)

                self.Message1 = Message(self.Frame1)
                self.Message1.place(relx=0.04, rely=0.11, relheight=0.84, relwidth=0.5)
                self.Message1.configure(background="#ffffff")
                self.Message1.configure(font=font11)
                self.Message1.configure(foreground="#000000")
                self.Message1.configure(highlightbackground="#ffffff")
                self.Message1.configure(highlightcolor="black")
                self.Message1.configure(text='''YOU CLICKED ON''')
                self.Message1.configure(width=496)

                self.Message2 = Message(self.Frame1)
                self.Message2.place(relx=0.52, rely=0.19, relheight=0.74, relwidth=0.07)
                self.Message2.configure(background="#ffffff")
                self.Message2.configure(font=font11)
                self.Message2.configure(foreground="#000000")
                self.Message2.configure(highlightbackground="#ffffff")
                self.Message2.configure(highlightcolor="black")
                self.Message2.configure(text=''':''')
                self.Message2.configure(width=66)

                self.Message3 = Message(self.Frame1)
                self.Message3.place(relx=0.57, rely=0.11, relheight=0.79, relwidth=0.35)
                self.Message3.configure(background="#ffffff")
                self.Message3.configure(font=font11)
                self.Message3.configure(foreground="#000000")
                self.Message3.configure(highlightbackground="#ffffff")
                self.Message3.configure(highlightcolor="black")
                self.Message3.configure(text='''CHECK INN''')
                self.Message3.configure(width=347)

                self.menubar = Menu(root,font=font9,bg=_bgcolor,fg=_fgcolor)
                root.configure(menu = self.menubar)



                self.Frame2 = Frame(root)
                self.Frame2.place(relx=0.03, rely=0.18, relheight=0.46, relwidth=0.93)
                self.Frame2.configure(relief=GROOVE)
                self.Frame2.configure(borderwidth="2")
                self.Frame2.configure(relief=GROOVE)
                self.Frame2.configure(background="#ffffff")
                self.Frame2.configure(highlightbackground="#ffffff")
                self.Frame2.configure(highlightcolor="black")
                self.Frame2.configure(width=995)

                self.Label3 = Label(self.Frame2)
                self.Label3.place(relx=0.05, rely=0.03, height=47, width=289)
                self.Label3.configure(activebackground="#ffffff")
                self.Label3.configure(activeforeground="black")
                self.Label3.configure(background="#ffffff")
                self.Label3.configure(disabledforeground="#bfbfbf")
                self.Label3.configure(font=font12)
                self.Label3.configure(foreground="#000000")
                self.Label3.configure(highlightbackground="#ffffff")
                self.Label3.configure(highlightcolor="black")
                self.Label3.configure(text='''ENTER YOUR NAME''')

                self.Label4 = Label(self.Frame2)
                self.Label4.place(relx=0.045, rely=0.29, height=47, width=329)
                self.Label4.configure(activebackground="#ffffff")
                self.Label4.configure(activeforeground="black")
                self.Label4.configure(background="#ffffff")
                self.Label4.configure(disabledforeground="#bfbfbf")
                self.Label4.configure(font=font12)
                self.Label4.configure(foreground="#000000")
                self.Label4.configure(highlightbackground="#ffffff")
                self.Label4.configure(highlightcolor="black")
                self.Label4.configure(text='''ENTER YOUR NUMBER''')



                self.Entry3 = Entry(self.Frame2)
                self.name=StringVar()
                self.Entry3.place(relx=0.47, rely=0.05,height=34, relwidth=0.43)
                self.Entry3.configure(background="white")
                self.Entry3.configure(disabledforeground="#bfbfbf")
                self.Entry3.configure(font=font10)
                self.Entry3.configure(foreground="#000000")
                self.Entry3.configure(highlightbackground="#ffffff")
                self.Entry3.configure(highlightcolor="black")
                self.Entry3.configure(insertbackground="black")
                self.Entry3.configure(selectbackground="#e6e6e6")
                self.Entry3.configure(selectforeground="black")
                self.Entry3.configure(textvariable=self.name)

                self.Entry4 = Entry(self.Frame2)
                self.mobile = StringVar()
                self.Entry4.place(relx=0.47, rely=0.31, height=34, relwidth=0.43)
                self.Entry4.configure(background="white")
                self.Entry4.configure(disabledforeground="#bfbfbf")
                self.Entry4.configure(font=font10)
                self.Entry4.configure(foreground="#000000")
                self.Entry4.configure(highlightbackground="#ffffff")
                self.Entry4.configure(highlightcolor="black")
                self.Entry4.configure(insertbackground="black")
                self.Entry4.configure(selectbackground="#e6e6e6")
                self.Entry4.configure(selectforeground="black")
                self.Entry4.configure(textvariable=self.mobile)

                self.Entry5 = Entry(self.Frame2)
                self.addr = StringVar()
                self.Entry5.place(relx=0.47, rely=0.18, height=34, relwidth=0.43)
                self.Entry5.configure(background="white")
                self.Entry5.configure(disabledforeground="#bfbfbf")
                self.Entry5.configure(font=font10)
                self.Entry5.configure(foreground="#000000")
                self.Entry5.configure(highlightbackground="#ffffff")
                self.Entry5.configure(highlightcolor="black")
                self.Entry5.configure(insertbackground="black")
                self.Entry5.configure(selectbackground="#e6e6e6")
                self.Entry5.configure(selectforeground="black")
                self.Entry5.configure(textvariable=self.addr)

                self.Label5 = Label(self.Frame2)
                self.Label5.place(relx=0.045, rely=0.16, height=47, width=334)
                self.Label5.configure(activebackground="#ffffff")
                self.Label5.configure(activeforeground="black")
                self.Label5.configure(background="#ffffff")
                self.Label5.configure(disabledforeground="#bfbfbf")
                self.Label5.configure(font=font12)
                self.Label5.configure(foreground="#000000")
                self.Label5.configure(highlightbackground="#ffffff")
                self.Label5.configure(highlightcolor="black")
                self.Label5.configure(text='''ENTER YOUR ADDRESS''')

                self.Label6 = Label(self.Frame2)
                self.Label6.place(relx=0.32, rely=0.5, height=48, width=296)
                self.Label6.configure(activebackground="#ffffff")
                self.Label6.configure(activeforeground="black")
                self.Label6.configure(background="#ffffff")
                self.Label6.configure(disabledforeground="#bfbfbf")
                self.Label6.configure(font=font13)
                self.Label6.configure(foreground="#000000")
                self.Label6.configure(highlightbackground="#ffffff")
                self.Label6.configure(highlightcolor="black")
                self.Label6.configure(text='''CHOOSE YOUR ROOM''')

                self.Label7 = Label(self.Frame2)
                self.Label7.place(relx=0.3, rely=0.79, height=48, width=300)
                self.Label7.configure(activebackground="#ffffff")
                self.Label7.configure(activeforeground="black")
                self.Label7.configure(background="#ffffff")
                self.Label7.configure(disabledforeground="#bfbfbf")
                self.Label7.configure(font=font14)
                self.Label7.configure(foreground="#000000")
                self.Label7.configure(highlightbackground="#ffffff")
                self.Label7.configure(highlightcolor="black")
                self.Label7.configure(text='''CHOOSE PAYMENT METHOD''')

                self.Message4 = Message(self.Frame2)
                self.Message4.place(relx=0.41, rely=0.04, relheight=0.1, relwidth=0.05)
                self.Message4.configure(background="#ffffff")
                self.Message4.configure(font=font13)
                self.Message4.configure(foreground="#000000")
                self.Message4.configure(highlightbackground="#ffffff")
                self.Message4.configure(highlightcolor="black")
                self.Message4.configure(text=''':''')
                self.Message4.configure(width=46)

                self.Message5 = Message(self.Frame2)
                self.Message5.place(relx=0.42, rely=0.17, relheight=0.12, relwidth=0.03)
                self.Message5.configure(background="#ffffff")
                self.Message5.configure(font=font13)
                self.Message5.configure(foreground="#000000")
                self.Message5.configure(highlightbackground="#ffffff")
                self.Message5.configure(highlightcolor="black")
                self.Message5.configure(text=''':''')
                self.Message5.configure(width=26)