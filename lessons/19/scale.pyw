#!/usr/bin/env python3.1

from tkinter import *

class Application(object):
    def __init__(self, parent):

        self.parent= parent

        self.quality = IntVar()
        self.quality.set(10)

        self.qualityScale = Scale(
            self.parent,
            variable=self.quality,
            from_=0,
            to=60,
            orient=HORIZONTAL,
            length=200,
            sliderlength=15
            )

        self.qualityScale.pack()

        self.imq=PhotoImage(file='exit.gif')
    
        self.QuitButton=Button(
            self.parent,
            image=self.imq,
            command=self.Quit
            )
        self.QuitButton.pack()

        self.parent.title('Example')

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
