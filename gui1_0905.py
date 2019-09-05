from tkinter import *
# 創建元件(指定老爸是誰)
# 立刻排版! (Grid/Pack)

def click():
    global e1
    global l2
    word = e1.get()
    l2["text"] = word.upper()

window = Tk()
window.title("第一個GUI程式")
window.geometry("500x500+200+200")

f1 = Frame(window, bg="orange")
f1.pack(expand=True, fill=BOTH)
l1 = Label(f1, text="請輸入英文單字")
l1.pack()
e1 = Entry(f1)
e1.pack()
b1 = Button(f1,
            bg="gold",
            text="按上面得到大寫",
            command=click)
b1.pack()
l2 = Label(f1, text="看結果")
l2.pack()

window.mainloop()