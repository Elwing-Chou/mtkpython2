from model import Base
from model import Student, Mobile
from tkinter import *
class MyFrame(LabelFrame):
    def __init__(self, master):
        LabelFrame.__init__(self, master, text="查詢電話")
        self.e1 = Entry(self)
        self.e1.pack(padx=20, pady=20)
        self.b1 = Button(self, text="查詢")
        self.b1.pack(padx=20, pady=20)
        self.result = Label(self, text="請按上面來查詢")
        self.result.pack(padx=20, pady=20)

window = Tk()
f1 = MyFrame(window)
f1.pack()
window.mainloop()
