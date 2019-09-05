from tkinter import *
from jieba.analyse import extract_tags
class MyFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.l1 = Label(self, text="輸入新聞")
        self.l1.pack()
        self.t1 = Text(self)
        self.t1.pack()
        self.b1 = Button(self,
                         text="分析",
                         command=self.analyse)
        self.b1.pack()
        self.result = Label(self, text="按『分析』得到結果")
        self.result.pack()

    def analyse(self):
        news = self.t1.get("1.0", "end")
        self.result["text"] = str(extract_tags(news, 5))

window = Tk()
f1 = MyFrame(window)
f1.pack(expand=True, fill=BOTH, padx=20, pady=20)
window.mainloop()