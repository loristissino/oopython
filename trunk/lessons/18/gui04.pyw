#!/usr/bin/env python3.1

from tkinter import * 

root = Tk()

MyLabel1 = Label(root, text="Prima etichetta.")
MyLabel1['background']="#FFFFFF"
MyLabel1['foreground']="red"
MyLabel1.pack({"side":"right"})
MyLabel1.pack()

MyLabel2 = Label(root, text="Seconda etichetta.")
MyLabel2['background']="#FFFFFF"
MyLabel2['foreground']="blue"
MyLabel2.pack({"side":"left"})


root.mainloop() 

