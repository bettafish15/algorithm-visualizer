import tkinter as tk

class sorting(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.grab_set()
        self.title(parent.tkvar.get())