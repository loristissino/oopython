#!/usr/bin/env python3.1

from tkinter import *

class Application(object):
    def __init__(self, parent):

        self.parent= parent

        self.img=PhotoImage(file='goldenstar.gif')
        self.ims=PhotoImage(file='silverstar.gif')
        self.imq=PhotoImage(file='exit.gif')

        self.StarButton=Button(
            self.parent,
            image=self.img,
            command=self.Toggle
            )

        self.isGold=True
        self.StarButton.pack()
    
        self.QuitButton=Button(
            self.parent,
            image=self.imq,
            command=self.Quit
            )
        self.QuitButton.pack()

    def Toggle(self):
        self.isGold = not self.isGold
        self.StarButton['image']=self.img if self.isGold else self.ims
        

    def Quit(self):
        self.parent.destroy()
        

def main():
    root = Tk()
    myapp = Application(root)
    
    root.mainloop() 

if __name__=='__main__':
    main()
