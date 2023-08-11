import tkinter.ttk as ttk
import tkinter as tk
from threading import Thread
import time

janela = tk.Tk()




janela.mainloop()

'''
class Main(object):
    def __init__(self, master):
        self.master = master

        self.frame = tk.Frame(self.master, width=400, height=400)
        self.frame.pack(expand=True)

        self.button = tk.Button(self.frame, text="Add Bar", command=lambda:self.createBar())
        self.button.pack(fill="y")

    def createBar(self):
        self.t = Thread(target=self.create)
        self.t.start()

    def create(self):
        newBar = LoadingBar(self.master, self.frame)

class LoadingBar(object):
    def __init__(self, master, frame):
        # Must use same Tkinter frame to add loading bars into
        self.master = master
        self.frame = frame
        self.add_bar()

    def start_thread(self):
        self.t = Thread(target=self.add_bar)
        self.t.start()

    def add_bar(self):
        self.var = tk.IntVar()
        self.var.set(0)

        self.progessbar = ttk.Progressbar(self.frame, variable=self.var, orient=tk.HORIZONTAL, length=200)
        self.progessbar.pack()

        self.add_values(self.var)

    def add_values(self, var):
        self.variable = var
        for self.x in range(100):
            time.sleep(0.1)
            self.variable.set(self.x)

root = tk.Tk()
app = Main(root)
root.mainloop()'''
