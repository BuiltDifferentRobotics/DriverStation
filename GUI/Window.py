import tkinter
from tkinter import *
from input import Input_Handler

class Window():

    top = tkinter.Tk()

    joystick = IntVar(top)
    jstest = Input_Handler.JSTest()
    string_var = StringVar(self.top)

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
        self.create_scale()
        self.string_var.set("Enabled: "+str(jstest.enabled)+" \n Autonomous: "+str(jstest.autonomous))
        label = Label(self.top, textvariable=self.string_var, relief=RAISED)
        label.pack()
        self.top.bind('<space>', self.disable)
        self.top.mainloop()

    def enable(self, event=None):
        jstest.enabled = 1
        self.string_var.set("Enabled: "+str(jstest.enabled)+" \n Autonomous: "+str(jstest.autonomous))

    def disable(self, event=None):
        jstest.enabled = 0
        self.string_var.set("Enabled: "+str(jstest.enabled)+" \n Autonomous: "+str(jstest.autonomous))

    def autonomous_trigger(self, event=None):
        jstest.autonomous = 1
        self.string_var.set("Enabled: "+str(jstest.enabled)+" \n Autonomous: "+str(jstest.autonomous))

    def teleop_trigger(self, event=None):
        jstest.autonomous= 0
        self.string_var.set("Enabled: "+str(jstest.enabled)+" \n Autonomous: "+str(jstest.autonomous))

    def create_scale(self, event=None):
        self.joystick.set(16)
        scale = Scale(self.top, variable = self.joystick, from_=0, to=256, tickinterval=64)
        scale.pack()

    def increment(self, event=None):
        self.joystick.set(self.joystick.get()+16)

def main():
    """Process all events forever."""
    win = Window()
    while 1:
        win.mainloop()
        win.jstest.process_events()

if __name__ == '__main__':
    main()