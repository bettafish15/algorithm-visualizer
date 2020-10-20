import tkinter as tk
import random


def swap(canvas, bar1, bar2):
    x1, _, x2, _ = canvas.coords(bar1)
    x3, _, x4, _ = canvas.coords(bar2)
    canvas.move(bar1, x4-x2, 0)
    canvas.move(bar2, x1-x3, 0)


def generate(canvas):
    canvas.delete("all")
    barStart = 5
    barEnd = 15
    global barList
    global lengthList
    lengthList = []
    barList = []
    shortest = [0, 345]
    longest = [0, 0]

    for bar in range(1, 60):
        randomY = random.randint(10, 340)
        while randomY in lengthList:
            randomY = random.randint(10, 340)
        lengthList.append(randomY)
        if randomY > longest[1]:
            longest[0] = bar
            longest[1] = randomY
        if randomY < shortest[1]:
            shortest[0] = bar
            shortest[1] = randomY
        bar = canvas.create_rectangle(
            barStart, randomY, barEnd, 350, fill='yellow')
        barList.append(bar)
        barStart += 10
        barEnd += 10

    canvas.itemconfig(barList[shortest[0]-1], fill="black")
    canvas.itemconfig(barList[longest[0]-1], fill="red")

# Algorithm


def bubbleSort(canvas, tk):
    global worker
    worker = _bubbleSort(canvas)
    animate(tk)


def _bubbleSort(canvas):
    global barList
    global lengthList
    for i in range(len(lengthList)):
        for j in range(len(lengthList) - i - 1):
            if lengthList[j] < lengthList[j+1]:
                lengthList[j], lengthList[j+1] = lengthList[j+1], lengthList[j]
                barList[j], barList[j+1] = barList[j+1], barList[j]
                swap(canvas, barList[j], barList[j+1])
                yield


def insertionSort(canvas, tk):
    global worker
    worker = _insertionSort(canvas)
    animate(tk)


def _insertionSort(canvas):
    global barList
    global lengthList
    for i in range(1, len(lengthList), 1):
        key = lengthList[i]
        j = i - 1
        while j >= 0 and lengthList[j] < key:
            lengthList[j+1] = lengthList[j]
            barList[j+1], barList[j] = barList[j], barList[j+1]
            swap(canvas, barList[j+1], barList[j])
            yield
            j = j - 1
        
        lengthList[j+1] = key
        
def selectionSort(canvas, tk):
    global worker
    worker = _selectionSort(canvas)
    animate(tk)


def _selectionSort(canvas):
    global barList
    global lengthList
    for i in range(0, len(lengthList)-1):
        minIndex = i
        for j in range(i+1, len(lengthList)):
            if lengthList[j] > lengthList[minIndex]:
                minIndex = j
        
        lengthList[minIndex], lengthList[i] = lengthList[i], lengthList[minIndex]
        swap(canvas, barList[i], barList[minIndex])
        barList[minIndex], barList[i] = barList[i], barList[minIndex]
        yield

    

##########################

def animate(tk):
    global worker
    if worker is not None:
        try:
            next(worker)
            tk.after(10, lambda: animate(tk))
        except StopIteration:
            worker = None


class sorting(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.grab_set()
        self.title(parent.tkvar.get())

        self.geometry('600x450')
        canvas = tk.Canvas(self, width='600', height='400')

        canvas.grid(column=0, row=0, columnspan=40)

        insert = tk.Button(self, text='Insertion Sort',
                           command=lambda: insertionSort(canvas, self))
        select = tk.Button(self, text='Selection Sort',
                           command=lambda: selectionSort(canvas, self))
        bubble = tk.Button(self, text='Bubble Sort',
                           command=lambda: bubbleSort(canvas, self))
        shuf = tk.Button(self, text='Shuffle',
                         command=lambda: generate(canvas))
        insert.grid(column=1, row=1)
        select.grid(column=2, row=1)
        bubble.grid(column=3, row=1)
        shuf.grid(column=0, row=1)

        generate(canvas)
