#!/usr/bin/env python3.1

from tkinter import *

class Application(object):
    def __init__(self, parent):

        self.UpperFrame=Frame(parent)
        self.MiddleFrame=Frame(parent)
        self.BottomFrame=Frame(parent)

        self.b1 = Button(self.UpperFrame, text="1")
        self.b2 = Button(self.UpperFrame, text="2")
        self.b3 = Button(self.UpperFrame, text="3")

        for widget in self.b1, self.b2, self.b3:
            widget.pack({'side':'left'})
            
        self.b4 = Button(self.MiddleFrame, text="4")
        self.b5 = Button(self.MiddleFrame, text="5")
        self.b6 = Button(self.MiddleFrame, text="6")

        for widget in self.b4, self.b5, s.elf.b6:
            widget.pack({'side':'left'})
        
        self.b7 = Button(self.BottomFrame, text="7")
        self.b8 = Button(self.BottomFrame, text="8")
        self.b9 = Button(self.BottomFrame, text="9")

        for widget in self.b7, self.b8, self.b9:
            widget.pack({'side':'left'})
            
        self.UpperFrame.pack({'side':'top'})
        self.MiddleFrame.pack({'side':'top'})
        self.BottomFrame.pack({'side':'top'})
        
def main():
    root = Tk()
    myapp = Application(root)
    root.mainloop() 

if __name__=='__main__':
    main()
    
