#!/usr/bin/env python3.1

from tkinter import * 

def MyButton_Click():
    StatusBar["text"]=name.get()

root = Tk()

name = StringVar()

MyInputBox = Entry(root, textvariable=name)
MyInputBox.pack()

MyButton = Button(root, text="Fai clic qui")
MyButton['background']="#FFFFFF"
MyButton['foreground']="red"
MyButton['command']=MyButton_Click
MyButton.pack({"side":"top", "padx": 10, "pady": 20})

StatusBar = Label(root, text="...")
StatusBar['background']="#FFFFFF"
StatusBar['foreground']="blue"
StatusBar.pack({"side":"bottom", "expand":"yes", "fill":"x"})

root.mainloop() 

