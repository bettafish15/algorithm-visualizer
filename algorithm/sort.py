import tkinter as tk


class sorting(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.grab_set()
        self.title(parent.tkvar.get())

        self.geometry('600x450')
        canvas = tk.Canvas(self, width='600', height='400')

        canvas.grid(column=0, row=0, columnspan=40)

        insert = tk.Button(self, text='Insertion Sort')
        select = tk.Button(self, text='Selection Sort')
        bubble = tk.Button(self, text='Bubble Sort')
        shuf = tk.Button(self, text='Shuffle')
        insert.grid(column=1,row=1)
        select.grid(column=2,row=1)
        bubble.grid(column=3,row=1)
        shuf.grid(column=0, row=1)