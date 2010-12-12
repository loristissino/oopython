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
        
        self.name = StringVar()
        self.buttons=[]
        self.parent = parent

        self.MyInputBox = Entry(parent, textvariable=self.name)
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
        self.StatusBar["text"]=self.name.get()
        n=str2int(self.name.get())
        for i in range(n):
            b=Button(self.parent, text="pulsante " + str(i))
            b['background']='yellow'
            b['command']=self.BuildButtonAction(i)
            b.pack()
            self.buttons.append(b)

    def BuildButtonAction(self, number):
        action = lambda n=number: self.ChangeButtonColor(n)
        return action

    def ChangeButtonColor(self, number):
        self._SwitchColor(self.buttons[number])
        #self._RemoveButton(self.buttons[number])
        
    def _SwitchColor(self, button):
        button['background']='yellow' if button['background']=='red' else 'red'
        
    def _RemoveButton(self, button):
        button.destroy()
        self.buttons.pop(button)

def main():
    root = Tk()
    myapp = Application(root)
    root.mainloop() 

if __name__=='__main__':
    main()
    
