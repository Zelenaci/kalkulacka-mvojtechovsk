#!/usr/bin/env python3
# Soubor:  kalkulacka.py
# Datum:   28.03.2022 08:31
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
############################################################################
import math
from os.path import basename, splitext
import tkinter as tk

# from tkinter import ttk

zasobnik = []
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

        self.var_entry = tk.IntVar()
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Kalkulačka")
        self.lbl.pack()
        self.entry = tk.Entry(self, textvariable= self.var_entry)
        self.entry.pack()
        self.btn2 = tk.Button(self, text="Zapsat hodnotu", command=self.zpracuj)
        self.btn2.pack()
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()

    def quit(self, event=None):
        super().quit()


    def operace(self, token):
        if token.upper() == "Q":
            exit()
        if token.upper() == "PI":
            zasobnik.append(math.pi)
        if token.upper() == "SW":
            b = zasobnik.pop()
            a = zasobnik.pop()
            zasobnik.append(b)
            zasobnik.append(a)
        if token in dva_operandy.keys():
            if len(zasobnik) >= 2:
                b = zasobnik.pop()
                a = zasobnik.pop()
                zasobnik.append(dva_operandy[token](a, b))
            else:
                print("Nemám dost operandů!!!")
        if token in jeden_operand.keys():
            if len(zasobnik) >= 1:
                a = zasobnik.pop()
                zasobnik.append(jeden_operand[token](a))
            else:
                print("Nemám dost operandů!!!")


    def zpracuj(self):
        token = self.var_entry.get()
        try:
            zasobnik.append(float(token))
        except ValueError:
            operace(self,token)


app = Application()
app.mainloop()

