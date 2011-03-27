#!/usr/bin/env python3.1

from tkinter import *

class Application(object):
    def __init__(self, parent):
        
        self.parent = parent

        self.OkButton=Button(self.parent, text='Return 0 value (it means you won)', command=self.OkButton_Click)
        self.OkButton.pack()

        self.FailedButton=Button(self.parent, text='Return 1 value (it means you lost)', command=self.FailedButton_Click)
        self.FailedButton.pack()

        self.returnValue=1
        # if we exit with 1, it means that the user closed the window

    def OkButton_Click(self):
        self.returnValue=0
        # the user won
        self.parent.destroy()

    def FailedButton_Click(self):
        self.returnValue=2
        # the user lost
        self.parent.destroy()

def main():
    root = Tk()
    myapp = Application(root)
    root.mainloop()
    return myapp.returnValue

if __name__=='__main__':
    sys.exit(main())
    
