#!/usr/bin/env python3.1

from tkinter import *

class Application(object):
    def __init__(self, parent):

        self.parent= parent

        SCALE_X=30
        OFFSET_X=10
        SCALE_Y=40
        OFFSET_Y=60

        self.digitButtons = []

        for digit in range(9):
            digitButton = Button(parent, text=str(digit+1))
            digitButton.place(
                y=(digit//3)*SCALE_Y+OFFSET_Y,
                x=(digit%3)*SCALE_X+OFFSET_X
                )
            self.digitButtons.append(digitButton)

        self.QuitButton=Button(parent, text='quit')
        self.QuitButton['command'] = self.Quit
        self.QuitButton.place(relx=0.7, rely=0.8)

    def Quit(self):
        self.parent.destroy()
        
def main():
    root = Tk()
    myapp = Application(root)
    root.mainloop() 

if __name__=='__main__':
    main()
    
