#!/usr/bin/env python3.1

from tkinter import *

class Application(object):
    def __init__(self, parent):

        self.parent= parent


        self.fruitListbox=Listbox(
            self.parent,
            height=5,
            selectmode='extended'
            )

        self.fruits=('apples', 'oranges', 'strawberries', 'bananas', 'lemons')

        for f in self.fruits:
            self.fruitListbox.insert("end", f)
            
        
        self.fruitListbox.pack()

        self.ReadButton=Button(
            self.parent,
            text="Tell me",
            command=self.ReadButton_Click
            )
        self.ReadButton.pack()

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
        self.OutputLabel['text']=self.fruitListbox.curselection()
        """
        t=''
        for f in self.fruitListbox.curselection():
            t+=self.fruits[int(f)]+' '
        self.OutputLabel['text']=t
        """


    def Quit(self):
        self.parent.destroy()
        

def main():
    root = Tk()
    myapp = Application(root)
    
    root.mainloop() 

if __name__=='__main__':
    main()
