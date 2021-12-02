from tkinter import *

class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidget(self):
        self.helloLable=Label(self,text='Hello world')
        self.helloLable.pack()
        self.quitButten=Button(self,text='quit',command=self.quit)
        self.quitButten.pack()

app=App()
app.master.title('hello world')
app.mainloop
