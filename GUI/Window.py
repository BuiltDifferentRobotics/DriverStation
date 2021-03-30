import tkinter
from tkinter import *
from input import Input_handler

class Window():

    top = tkinter.Tk()

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
        self.top.bind('f', self.f)
        self.top.bind('<space>', self.disable)
        self.top.mainloop()

    def enable(self, event=None):
        Input_handler.enabled = 1

    def disable(self, event=None):
        Input_handler.enabled = 0

    def autonomous_trigger(self, event=None):
        Input_handler.autonomous = 1

    def teleop_trigger(self, event=None):
        Input_handler.autonomous= 0

def main():
    """Process all events forever."""
    win = Window()
    jstest = Input_handler.JSTest()
    while 1:
        win.mainloop()
        jstest.process_events()

if __name__ == '__main__':
    main()