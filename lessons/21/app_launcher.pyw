#!/usr/bin/env python3.1

from tkinter import *
import subprocess
import sys
import os

def interpretername():
    commands={
        'posix':'python3.1',
        'nt':'pyhton31.exe',
        }
    return commands.get(os.name)

class Application(object):
    def __init__(self, parent):
        
        self.parent = parent

        self.other = Button(self.parent, text='Launch the game', command=self.Other_Click)
        self.other.pack()

        self.statusbar = Label(self.parent, text='')
        self.statusbar.pack()

    def Other_Click(self):
        self.statusbar['text']='Game started...'
        
        self.parent.update_idletasks()
        # if we don't call this, the label will not be redrawn
        
        try:
            subprocess.check_output([interpretername(), 'thegame.pyw'])
            # sys.path[1] is the name of the python interpreter invoked.
            # here, we use the same one for the called program.
            self.statusbar['text']='You won!'
        except:
            self.statusbar['text']='You lose!'
        
def main():
    root = Tk()
    myapp = Application(root)
    root.mainloop() 

if __name__=='__main__':
    main()
    
