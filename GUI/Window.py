import tkinter
from tkinter import *

class Window():

    top = tkinter.Tk()
    enabled = 0
    autonomous = 0

    def __init__(self):
        pass

    def mainloop(self):
        test = Button(self.top, text = "Enable", command = self.enable)
        test.pack()
        test = Button(self.top, text = "Disable", command = self.disable)
        test.pack()
        test = Button(self.top, text="autonomous", command=self.autonomous_trigger)
        test.pack()
        test = Button(self.top, text="Teleop", command=self.teleop_trigger)
        test.pack()
        test = Button(self.top, text="Debug: Print state", command=self.print_state)
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

    def autonomous_trigger(self, event=None):
        self.autonomous = 1
        print(self.autonomous)

    def teleop_trigger(self, event=None):
        self.autonomous= 0
        print(self.autonomous)

    def print_state(self, event=None):
        print("enabled: "+str(self.enabled))
        print("autonomous: " + str(self.autonomous))

    def f(self, event=None):
        print('f to pay respecs')

if __name__ == '__main__':
    win = Window()
    win.mainloop()