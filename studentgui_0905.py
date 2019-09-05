from tkinter import *
from models import *
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class QueryFrame(Frame):
    def __init__(self, master, engine):
        Frame.__init__(self, master)

        S = sessionmaker(bind=engine)
        self.session = S()

        self.l1 = Label(self, text="輸入學生姓名")
        self.l1.pack()
        self.e1 = Entry(self)
        self.e1.pack()
        self.b1 = Button(self, text="查詢", command=self.query)
        self.b1.pack()
        self.result = Label(self, text="按『查詢』得到結果")
        self.result.pack()

    def query(self):
        name = self.e1.get()

window = Tk()

dn = os.path.dirname(__file__)
fn = "sqlite:///" + os.path.join(dn, "data.sqlite")
en = create_engine(fn, echo=False)

f1 = QueryFrame(window, en)
f1.pack(padx=20, pady=20)
window.mainloop()