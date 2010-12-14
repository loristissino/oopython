#!/usr/bin/env python3.1

from tkinter import *

def str2int(s):
    try:
        k=int(s)
        return k
    except:
        return 0

class Application(object):
    def __init__(self, parent):
        
        self.propertyname = StringVar()
        self.propertyname.set('selectforeground') # valore di default
        self.propertyvalue = StringVar()
        self.propertyvalue.set('green')
        self.parent = parent

        properties = ['background',
                      'foreground',
                      'activebackground',
                      'disabledforeground',
                      'highlightcolor',
                      'highlightbackground',
                      'width',
                      'height',
                      'padx',
                      'pady',
                      ]

        self.PropertyMenu = OptionMenu(parent, self.propertyname, *properties)
        self.PropertyMenu.pack()

        self.MyInputBox = Entry(parent, textvariable=self.propertyvalue)
        self.MyInputBox.pack()

        self.MyButton = Button(parent, text="Fai clic qui")
        self.MyButton['background']="#FFFFFF"
        self.MyButton['foreground']="red"
        self.MyButton['command']=self.MyButton_Click
        self.MyButton.pack({"side":"top", "padx": 10, "pady": 20})

        self.StatusBar = Label(parent, text="...")
        self.StatusBar['background']="#FFFFFF"
        self.StatusBar['foreground']="blue"
        self.StatusBar.pack({"side":"bottom", "expand":"yes", "fill":"x"})

    def MyButton_Click(self):
        print('name:', self.propertyname.get())
        print('value', self.propertyvalue.get())
        self.MyButton[self.propertyname.get()]=self.propertyvalue.get()


def main():
    root = Tk()
    myapp = Application(root)
    root.mainloop() 

if __name__=='__main__':
    main()
    
