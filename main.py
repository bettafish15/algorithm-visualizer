import inspect
import tkinter as tk  # python 3
from tkinter import font
from tkinter import ttk
import algorithm


class mainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Algorithm Visualizer")
        self.geometry("320x100")
        ttk.Label(
            self,
            text="Choose algorithm: ",
            font=font.Font(family="Times New Roman", size=10),
        ).grid(column=0, row=5, padx=10, pady=25)

        self.tkvar = tk.StringVar(self)
        algoList = ttk.Combobox(
            self, state="readonly", width=20, textvariable=self.tkvar
        )

        array_temp = []

        for i, element in inspect.getmembers(algorithm):
            if inspect.isclass(element):
                array_temp.append(i)

        algoList["values"] = tuple(array_temp)
        algoList.current(0)
        algoList.grid(column=1, row=5)

        tk.Button(
            self,
            text="Start",
            command=lambda: getattr(algorithm, self.tkvar.get())(self),
        ).grid(column=100, row=5, padx=5, pady=5)


if __name__ == "__main__":
    app = mainApp()
    app.mainloop()
