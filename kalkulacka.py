#!/usr/bin/env python3
# Soubor:  kalkulacka.py
# Datum:   28.03.2022 08:31
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
############################################################################
from asyncio import events
from inspect import Parameter
import math
from os.path import basename, splitext
import tkinter as tk
from traceback import print_tb

# from tkinter import ttk


dva_operandy = {}
dva_operandy["+"] = lambda a, b: a + b
dva_operandy["-"] = lambda a, b: a - b
dva_operandy["*"] = lambda a, b: a * b
dva_operandy["/"] = lambda a, b: a / b
dva_operandy["//"] = lambda a, b: a // b
dva_operandy["**"] = lambda a, b: a ** b

jeden_operand = {}
jeden_operand["sin"] = math.sin
jeden_operand["cos"] = math.cos
jeden_operand["tg"] = math.tan
jeden_operand["tan"] = math.tan


class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, class_=parent.name)
        self.config()

        btn = tk.Button(self, text="Konec", command=self.close)
        btn.pack()

    def close(self):
        self.destroy()


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Kalkulkačka"

    def __init__(self):

        super().__init__(className=self.name)

        self.zasobnik = []
        self.var_entry = tk.IntVar()
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Kalkulačka")
        self.lbl.grid(column=1)
        self.entry = tk.Entry(self, textvariable= self.var_entry)
        self.entry.grid()
        self.btn2 = tk.Button(self, text="Zapsat hodnotu", command=self.fce)
        self.btn2.grid()
        self.btnUp = tk.Button(self, text="Dolů",command=self.posunUp)
        self.btnUp.grid(row=1, column=2)
        self.btnDown = tk.Button(self, text="Nahoru",command=self.posunDown)
        self.btnDown.grid(row=1, column=4)
        self.listBox = tk.Listbox(self)
        self.listBox.grid(row=1,column=1)
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.grid(column=1)

    def quit(self, event=None):
        super().quit()

    def fce(self):
        self.zpracuj(self.entry.get())

    def operace(self, token, event=None):
            token = str(self.entry.get())
            if token.upper() == "Q":
                exit()
            if token.upper() == "PI":
                self.zasobnik.append(math.pi)
            if token.upper() == "SW":
                a =  self.listBox.get(tk.END)
                b =  self.listBox.get(tk.END-1)
                self.zasobnik.append(b)
                self.zasobnik.append(a)
            if token in dva_operandy.keys():
                if len(self.zasobnik) >= 2:
                    b = self.zasobnik.pop()
                    a = self.zasobnik.pop()
                    self.zasobnik.append(dva_operandy[token](a, b))
                else:
                    print("Nemám dost operandů!!!")
            if token in jeden_operand.keys():
                if len(self.zasobnik) >= 1:
                    a = self.zasobnik.pop()
                    self.zasobnik.append(jeden_operand[token](a))
                else:
                    print("Nemám dost operandů!!!")
            self.listBox.delete(0,tk.END)
            for token in self.zasobnik:
                self.listBox.insert(tk.END,token)
                

    def zpracuj(self, token,event=None):
        try:
            self.zasobnik.append(float(token))
            self.listBox.insert(tk.END,token)
        except ValueError:
            self.operace(self,token)
    
    def posunUp(self):
        active = self.listBox.get(tk.ACTIVE)
        for index in self.listBox.curselection():
            try:
                self.listBox.delete(index)
                self.listBox.insert(index+1, active)
                item = self.zasobnik[index]
                self.zasobnik[index] = self.zasobnik[index+1]
                self.zasobnik[index+1]= item
            except IndexError:
                print("krajní hondota nelze posunout")    


        

    def posunDown(self):
        active = self.listBox.get(tk.ACTIVE)
        for index in self.listBox.curselection():
            try:    
                self.listBox.delete(index)
                self.listBox.insert(index-1, active)
                item = self.zasobnik[index]
                self.zasobnik[index] = self.zasobnik[index-1]
                self.zasobnik[index-1]= item
            except IndexError:
                print("krajní hondota nelze posunout")    

app = Application()
app.mainloop()