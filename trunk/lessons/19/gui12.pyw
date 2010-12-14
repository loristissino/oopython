#!/usr/bin/env python3.1

from tkinter import *

class Application(object):
    def __init__(self, parent):

        self.parent= parent

        self.digitButtons = []

        for digit in range(9):
            digitButton = Button(parent, text=str(digit+1))
            digitButton.grid(row=digit//3, column=digit%3)
            self.digitButtons.append(digitButton)

        self.QuitButton=Button(parent, text='quit')
        self.QuitButton['command'] = self.Quit
        self.QuitButton.grid(row=4, column=4)

    def Quit(self):
        self.parent.destroy()
        
def main():
    root = Tk()
    myapp = Application(root)
    root.mainloop() 

if __name__=='__main__':
    main()
    
