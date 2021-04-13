import tkinter
from tkinter import *

import multiprocessing


from input import Input_Handl

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

def run_input_handler():
    while(1):
        print("input handler thread runs\n")
        #Window.joystickInput.process_events()

def run_window():
    while(1):
        print("window\n")

if __name__ == '__main__':
    #making a window
    window = Window()
    input = window.joystickInput

    input_process = multiprocessing.Process(target=window.joystickInput.main)
    window_process=multiprocessing.Process(target=window.mainloop)
    input_process.start()
    window_process.start()
    input_process.join()
    window_process.join()