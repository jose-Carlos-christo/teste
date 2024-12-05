import tkinter as tk
# -*- coding: utf-8 -*-

class Application(tk.Frame):
    def __init__(win, master=None):
        super().__init__(master)
        win.pack()
        win.criar_widgets()
        
    def criar_widgets(win):
        win.bt1 = tk.Button(win)
        win.bt1["text"] = "Olá Mundo\n(click Aqui)"
        win.bt1["command"] = win.diz_ola
        win.bt1.pack(side="top")

        win.bt_sair = tk.Button(win, text="SAIR", fg="blue",
                              command=root.destroy)
        win.bt_sair.pack(side="bottom")

    def diz_ola(win):
        print("Olá, Todo Mundo!")
        print(type(win))

root = tk.Tk()
app = Application(master=root)
app.mainloop()
