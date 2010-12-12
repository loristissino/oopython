#!/usr/bin/env python3.1

from tkinter import * 

class Application(object):
    def __init__(self, parent):
        
        self.name = StringVar()

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


def main():
    root = Tk()
    myapp = Application(root)
    root.mainloop() 

if __name__=='__main__':
    main()
    
