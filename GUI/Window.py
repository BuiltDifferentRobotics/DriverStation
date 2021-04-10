import tkinter
from tkinter import *

import threading

from input import Input_Handler


class Window():

    top = tkinter.Tk()

    string_var = StringVar(top)

    joystickInput = Input_Handler.JoystickI()

    def __init__(self):
        pass

    def mainloop(self):
        test = Button(self.top, text="Enable", command=self.enable)
        test.pack()
        test = Button(self.top, text="Disable", command=self.disable)
        test.pack()
        test = Button(self.top, text="autonomous", command=self.autonomous_trigger)
        test.pack()
        test = Button(self.top, text="Teleop", command=self.teleop_trigger)
        test.pack()

        self.string_var.set(
            "Enabled: " + str(self.joystickInput.enabled) + " \n Autonomous: " + str(self.joystickInput.autonomous))
        label = Label(self.top, textvariable=self.string_var, relief=RAISED)
        label.pack()
        while True:
            self.joystickInput.process_events()

            self.top.bind('<space>', self.disable)


            self.top.update_idletasks()
            self.top.update()

    def enable(self, event=None):
        self.joystickInput.enabled = 1
        self.string_var.set("Enabled: " + str(self.joystickInput.enabled) + " \n Autonomous: " + str(self.joystickInput.autonomous))

    def disable(self, event=None):
        self.joystickInput.enabled = 0
        self.string_var.set("Enabled: " + str(self.joystickInput.enabled) + " \n Autonomous: " + str(self.joystickInput.autonomous))

    def autonomous_trigger(self, event=None):
        self.joystickInput.autonomous = 1
        self.string_var.set("Enabled: " + str(self.joystickInput.enabled) + " \n Autonomous: " + str(self.joystickInput.autonomous))

    def teleop_trigger(self, event=None):
        self.joystickInput.autonomous= 0
        self.string_var.set("Enabled: " + str(self.joystickInput.enabled) + " \n Autonomous: " + str(self.joystickInput.autonomous))

def main():
    """Process all events forever."""
    win = Window()
    win.mainloop()

class InputThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        run_input_handler(self.name)
        print("Exiting" + self.name)


class WindowThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        run_window(self.name)
        print("Exiting" + self.name)

def run_input_handler(thread):
    while(1):
        print("input handler thread runs\n")
        #indow.joystickInput.process_events()

def run_window(thread):
    #Window.main()
    while(1):
        print("window thread runs \n")

if __name__ == '__main__':
    thread1 = InputThread(1, "thread1", 1)
    thread2 = WindowThread(2, "thread2", 2)

    thread1.start()
    thread2.start()