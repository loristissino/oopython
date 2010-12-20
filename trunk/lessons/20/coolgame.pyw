#!/usr/bin/env python3.1

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

class Application(object):

    def LeftButton_Click(self, event=None):
        if not self._gameover:
            self.Canvas.move(self.obj_id, -self.MOVEX, 0)
            self.CheckBorders()
        
    def RightButton_Click(self, event=None):
        if not self._gameover:
            self.Canvas.move(self.obj_id, self.MOVEX, 0)
            self.CheckBorders()
    
    def UpButton_Click(self, event=None):
        if not self._gameover:
            self.Canvas.move(self.obj_id, 0, -self.MOVEY)
            self.CheckBorders()

    def DownButton_Click(self, event=None):
        if not self._gameover:
            self.Canvas.move(self.obj_id, 0, self.MOVEY)
            self.CheckBorders()

    def MoveObjectDown(self):
        if not self._gameover:
            self.Canvas.move(self.obj_id, 0, self.FALLY)
            self.CheckBorders()
            self.parent.after(self.Delay.get(), self.MoveObjectDown)

    def GameOver(self):
        self._gameover=True
        self.Canvas.itemconfig(self.obj_id, fill='yellow')
        self.Canvas['cursor']='pirate'
        self.ToggleButtons('disabled')
        messagebox.showinfo(title=self.TITLE, message='--- GAME OVER ---')

    def ToggleButtons(self, state):
        for b in self.UpButton, self.DownButton, self.LeftButton, self.RightButton:
            b['state']=state

    def GameWon(self):
        self._gameover=True
        self.Canvas.itemconfig(self.obj_id, fill='white')
        self.Canvas['cursor']='pirate'
        self.ToggleButtons('disabled')
        messagebox.showinfo(title=self.TITLE, message='--- YOU WON! ---')
        

    def CheckBorders(self):
        x1,y1,x2,y2=self.Canvas.coords(self.obj_id)
        if y2>200:
            self.GameOver()
        if y1<0:
            self.GameWon()
        
    def __init__(self, parent):
        self.MOVEX=2
        self.MOVEY=2
        self.FALLY=1
        self.DELAY_VERYFAST=40
        self.DELAY_FAST=100
        self.DELAY_SLOW=300
        self.TITLE='THE BIG GAME'

        self.Delay=IntVar()
        self.Delay.set(self.DELAY_SLOW)

        self.parent= parent
        self._gameover = False

        self.Canvas = Canvas(self.parent, width=300, height=200)
        self.Canvas['background']='white'
        self.Canvas['cursor']='watch'
        self.Canvas.pack({'pady':10, 'padx':10})

        self.obj_id = self.Canvas.create_oval(120, 80, 180, 120, width=2, fill='red')

        self.UpFrame=Frame(self.parent)
        self.UpButton = Button(self.UpFrame, text="UP", command=self.UpButton_Click)
        self.UpButton.pack()
        self.UpFrame.pack()
        self.MiddleFrame=Frame(self.parent)
        self.LeftButton = Button(self.MiddleFrame, text="LEFT", command=self.LeftButton_Click)
        self.LeftButton.pack({'side':'left'})
        self.RightButton = Button(self.MiddleFrame, text="RIGHT", command=self.RightButton_Click)
        self.RightButton.pack({'side':'left'})
        self.MiddleFrame.pack()
        self.BottomFrame = Frame(self.parent)
        self.DownButton = Button(self.BottomFrame, text="DOWN", command=self.DownButton_Click)
        self.DownButton.pack()
        self.BottomFrame.pack()

        self.OptionsFrame=Frame(self.parent)
        self.SlowRadioButton=Radiobutton(self.OptionsFrame, text='Slow', variable=self.Delay, value=self.DELAY_SLOW).pack({'side':'left'})
        self.FastRadioButton=Radiobutton(self.OptionsFrame, text='Fast', variable=self.Delay, value=self.DELAY_FAST).pack({'side':'left'})
        self.VeryFastRadioButton=Radiobutton(self.OptionsFrame, text='Very fast', variable=self.Delay, value=self.DELAY_VERYFAST).pack({'side':'left'})
        self.OptionsFrame.pack()

        #binding degli eventi da tastiera
        self.parent.bind('<Up>', self.UpButton_Click)
        self.parent.bind('<Down>', self.DownButton_Click)
        self.parent.bind('<Left>', self.LeftButton_Click)
        self.parent.bind('<Right>', self.RightButton_Click)
        self.parent.bind('q', self.Quit)

        self.QuitButton=Button(parent, text='Quit')
        self.QuitButton['command'] = self.Quit
        self.QuitButton['underline']=0
        self.QuitButton.pack({'pady':20})

        self.parent.after(self.Delay.get(), self.MoveObjectDown)
        print(self.Delay.get())
        self.setMenu()

        self.parent.title(self.TITLE)

        self.parent.geometry('300x400')


    def setMenu(self):
        MenuBar = Menu(self.parent)
        self.parent['menu']=MenuBar

        FileMenu=Menu(MenuBar)
        FileMenu.add_command(label='Open…', command=self.FileLoad)
        FileMenu.add_command(label='Save as…', command=self.FileSave)
        FileMenu.add_command(label='Quit', command=self.Quit)

        HelpMenu=Menu(MenuBar)
        HelpMenu.add_command(label='About', command=self.HelpAbout)

        MenuBar.add_cascade(label='File', menu=FileMenu)
        MenuBar.add_cascade(label='Help', menu=HelpMenu)
        

        
    def Quit(self, event=None):
        self.parent.destroy()


    def FileLoad(self):
        ftypes = [('Text files', '*.txt'), ('XML Files', '*.xml'), ('All files', '*.*')]
        filename = filedialog.askopenfilename(title='Chose a file to open', filetypes=ftypes)
        if filename:
            messagebox.showinfo(title='File opening', message='I should open file ' + filename)

    def FileSave(self):
        ftypes = [('Text files', '*.txt'), ('XML Files', '*.xml'), ('All files', '*.*')]
        filename = filedialog.asksaveasfilename(title='Chose where to save data', filetypes=ftypes)
        if filename:
            messagebox.showinfo(title='File saving', message='I should save to file ' + filename)

    def HelpAbout(self):
        pass

    
        
def main():
    root = Tk()
    myapp = Application(root)
    root.mainloop() 

if __name__=='__main__':
    main()
