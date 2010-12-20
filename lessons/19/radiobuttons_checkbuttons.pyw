#!/usr/bin/env python3.1

from tkinter import *

class Application(object):
    def __init__(self, parent):

        self.parent= parent

        self.quality = IntVar()
        self.quality.set(10)

        f=Frame(self.parent)

        self.qualityRadiobutton_Low=Radiobutton(
            f,
            text='low quality',
            variable=self.quality,
            value=10
            )
        self.qualityRadiobutton_Middle=Radiobutton(
            f,
            text='middle quality',
            variable=self.quality,
            value=20
            )
        self.qualityRadiobutton_High=Radiobutton(
            f,
            text='high quality',
            variable=self.quality,
            value=30
            )

        self.qualityRadiobutton_Low.pack({'side':'left'})
        self.qualityRadiobutton_Middle.pack({'side':'left'})
        self.qualityRadiobutton_High.pack({'side':'left'})

        f.pack()

        self.full=BooleanVar()
        self.full.set(False)

        self.fullCheckbutton=Checkbutton(
            self.parent,
            text='full example',
            variable=self.full
            )
        self.fullCheckbutton.pack()

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
