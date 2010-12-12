#!/usr/bin/env python3.1

from tkinter import * 

root = Tk()

MyLabel = Label(root, text="The quick brown fox jumps over the lazy dog.")
MyLabel['background']="#FFFFFF"
MyLabel['foreground']="red"
MyLabel.pack()

root.mainloop() 

