import tkinter
from tkinter import *

class Window():

    top = tkinter.Tk()
    enabled = 0

    def __init__(self):
        pass

    def mainloop(self):
        test = Button(self.top, text = "Enable", command = self.enable)
        test.pack()
        test = Button(self.top, text = "Disable", command = self.disable)
        test.pack()
        test = Button(self.top, text="Tare", command=self.tare)
        test.pack()
        self.top.bind('f', self.f)
        self.top.bind('<space>', self.disable)
        self.top.mainloop()

    def enable(self, event=None):
        self.enabled = 1
        print(self.enabled)

    def disable(self, event=None):
        self.enabled = 0
        print(self.enabled)

    def f(self, event=None):
        print('f to pay respecs')

    def tare(self, event=None):
        self.enabled = 0

if __name__ == '__main__':
    win = Window()
    win.mainloop()