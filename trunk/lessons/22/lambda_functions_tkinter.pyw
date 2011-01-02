#!/usr/bin/env python3.1

from tkinter import *

class Application(object):
    def __init__(self, parent):
        self.parent=parent
        self.buttons=[]
        
        for i in range(10):
            b=Button(self.parent, text="pulsante %d" %i)
            b['background']='yellow'
            b['command']=self.BuildButtonAction(i)
            b.pack()
            self.buttons.append(b)

    def BuildButtonAction(self, number):
        return lambda : self.ChangeButtonColor(number)
        
    def ChangeButtonColor(self, number):
        self._SwitchColor(self.buttons[number])
        
    def _SwitchColor(self, button):
        button['background']='yellow' if button['background']=='red' else 'red'
        
def main():
    root = Tk()
    myapp = Application(root)
    root.mainloop() 

if __name__=='__main__':
    main()
    
