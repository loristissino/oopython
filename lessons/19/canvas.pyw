#!/usr/bin/env python3.1

from tkinter import *

class Application(object):
    def __init__(self, parent):

        self.Canvas = Canvas(parent, width=300, height=150)
        self.Canvas['background'] = 'white'
        self.Canvas.pack()

        self.r1_id = None

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
        if self.r1_id:
            self.Canvas.move(self.r1_id, 2, 5)
        else:
            self.r1_id = self.Canvas.create_rectangle(2, 10, 8, 20)

def main():
    root = Tk()
    myapp = Application(root)
    root.mainloop() 

if __name__=='__main__':
    main()
    
