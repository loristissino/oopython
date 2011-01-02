#!/usr/bin/env python3.1

import functools
from tkinter import *

class Application(object):
    def __init__(self, parent):
        self.parent=parent
        self.buttons=[]
        
        for i in range(5):
            b=Button(self.parent, text="pulsante %d" %i)
            b['background']='yellow'
            b['state']='disabled'
            b['command']=functools.partial(self.ChangeButtonColor, i)
            b.pack()
            self.buttons.append(b)

        self.PlayButton=Button(self.parent,
               text='Gioca',
               command=functools.partial(self.ExecuteCommand, 'play')
                )
        self.PlayButton.pack()
        self.QuitButton=Button(self.parent,
               text='Esci',
               command=functools.partial(self.ExecuteCommand, 'quit')
                )
        self.QuitButton.pack()
        
    def ChangeButtonColor(self, number):
        self._SwitchColor(self.buttons[number])
        
    def _SwitchColor(self, button):
        button['background']='yellow' if button['background']=='red' else 'red'

    def ExecuteCommand(self, command):
        if command=='quit':
            self.parent.destroy()
        if command=='play':
            self.StartGame()

    def StartGame(self):
        for button in self.buttons:
            button['state']='active'
        
def main():
    root = Tk()
    myapp = Application(root)
    root.mainloop() 

if __name__=='__main__':
    main()
    
