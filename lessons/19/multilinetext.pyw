#!/usr/bin/env python3.1

from tkinter import *

class Application(object):
    def __init__(self, parent):

        self.parent= parent

        self.lyricsFrame=Frame(self.parent)
        
        self.lyricsText = Text(self.lyricsFrame,
            width=80,
            height=4
            )
        self.lyricsText.pack({'side':'left'})

        self.lyricsText.insert("1.0",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nNam consectetur dictum nisl, eget blandit magna suscipit tristique.\nFusce sit amet nunc eu lorem varius luctus ac id eros.\nClass aptent taciti sociosqu ad litora torquent per conubia nostra,\nper inceptos himenaeos.")

        self.lyricsScrollbar=Scrollbar(self.lyricsFrame)
        self.lyricsScrollbar.pack({'side':'left', 'expand':'yes', 'fill':'y'})

        self.lyricsFrame.pack()

        self.lyricsScrollbar['command']=self.lyricsText.yview
        self.lyricsText['yscrollcommand']=self.lyricsScrollbar.set

        self.ReadButton=Button(
            self.parent,
            text="Tell me",
            command=self.ReadButton_Click
            )
        self.ReadButton.pack()

        self.DeleteButton=Button(
            self.parent,
            text="Delete some text",
            command=self.DeleteButton_Click
            )
        self.DeleteButton.pack()

        
        self.OutputLabel = Label(self.parent, text="")
        self.OutputLabel.pack()

        self.imq=PhotoImage(file='exit.gif')
    
        self.QuitButton=Button(
            self.parent,
            image=self.imq,
            command=self.Quit
            )
        self.QuitButton.pack()

        self.parent.title('Example')

    def ReadButton_Click(self):
        self.OutputLabel['text']=self.lyricsText.get("2.4", "end")

    def DeleteButton_Click(self):
        self.lyricsText.delete("2.4", "end")

    def Quit(self):
        self.parent.destroy()
        

def main():
    root = Tk()
    myapp = Application(root)
    
    root.mainloop() 

if __name__=='__main__':
    main()
