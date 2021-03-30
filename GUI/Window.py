import tkinter
from tkinter import *
from input import Input_Handler

class Window():

    top = tkinter.Tk()

    joystick = IntVar(top)

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
        var = StringVar(self.top)
        var.set("Enabled: "+str(Input_Handler.enabled)+" \n Autonomous: "+str(Input_Handler.autonomous))
        label = Label(self.top, textvariable=var, relief=RAISED)
        label.pack()
        self.top.bind('<space>', self.disable)
        self.top.mainloop()

    def enable(self, event=None):
        Input_Handler.enabled = 1
        var.set("Enabled: "+str(Input_Handler.enabled)+" \n Autonomous: "+str(Input_Handler.autonomous))

    def disable(self, event=None):
        Input_Handler.enabled = 0
        var.set("Enabled: "+str(Input_Handler.enabled)+" \n Autonomous: "+str(Input_Handler.autonomous))

    def autonomous_trigger(self, event=None):
        Input_Handler.autonomous = 1
        var.set("Enabled: "+str(Input_Handler.enabled)+" \n Autonomous: "+str(Input_Handler.autonomous))

    def teleop_trigger(self, event=None):
        Input_Handler.autonomous= 0
        var.set("Enabled: "+str(Input_Handler.enabled)+" \n Autonomous: "+str(Input_Handler.autonomous))

    def create_scale(self, event=None):
        self.joystick.set(16)
        scale = Scale(self.top, variable = self.joystick, from_=0, to=256, tickinterval=64)
        scale.pack()

    def increment(self, event=None):
        self.joystick.set(self.joystick.get()+16)

def main():
    """Process all events forever."""
    win = Window()
    jstest = Input_Handler.JSTest()
    while 1:
        win.mainloop()
        jstest.process_events()

if __name__ == '__main__':
    main()