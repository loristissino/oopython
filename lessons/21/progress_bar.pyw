#!/usr/bin/env python3.1

PROGRESS=3

from tkinter import *

class ProgressBar(object):
    def __init__(self, parent, height=10, width=300, background=None, foreground='black', progress=0):
        # adapted from "Python 2.1 Bible" (by Dave Brueck and Stephen Tanner)
        self._parent=parent
        self._height=height
        self._width=width
        self._background=background
        self._foreground=foreground

        self.barcanvas=Canvas(
            self._parent,
            width=self._width,
            heigh=self._height,
            background=self._background,
            borderwidth=1,
            relief=SUNKEN
            )
        self.barcanvas.pack(padx=5, pady=2)
        self.rectangleValue=self.barcanvas.create_rectangle(0,0,0, self._height)
        self.barcanvas.itemconfigure(
            self.rectangleValue,
            fill=self._foreground
            )

        self.setProgressPercent(progress)

    def getProgressPercent(self):
        return self._progress

    def setProgressPercent(self, level):
        self._progress = min(100, max(0, level))
        self.DrawProgress()

    def DrawProgress(self):
        pixels=round(self._width * self.getProgressPercent()/100.0)
        self.barcanvas.coords(
            self.rectangleValue,
            0,
            0,
            pixels,
            self._height
            )
            
    def pack(self, *args, **kwargs):
        self.barcanvas.pack(*args, **kwargs)

    def grid(self, *args, **kwargs):
        self.barcanvas.grid(*args, **kwargs)
        
    def place(self, *args, **kwargs):
        self.barcanvas.place(*args, **kwargs)


class Application(object):
    def __init__(self, parent):
        
        self.parent = parent
        self.PB = ProgressBar(self.parent, progress=0, foreground="red", width=400)
        self.PB.pack()

        self.forward = Button(self.parent, text='Forward', command=self.ForwardClick)
        self.forward.pack()
        
        self.back = Button(self.parent, text='Back', command=self.BackClick)
        self.back.pack()

        self.start = Button(self.parent, text='Start', command=self.StartClick)
        self.start.pack()

        self.stop = Button(self.parent, text='Stop', command=self.StopClick)
        self.stop['state']='disabled'
        self.stop.pack()

    def ForwardClick(self):
        print('forward')
        self.PB.setProgressPercent(self.PB.getProgressPercent()+PROGRESS)
    
    def BackClick(self):
        print('back')
        self.PB.setProgressPercent(self.PB.getProgressPercent()-PROGRESS)

    def StartClick(self):
        self.go=True
        self.stop['state']='active'
        self.DoSomething()

    def StopClick(self):
        self.go=False

    def DoSomething(self):
        if self.PB.getProgressPercent() % 10 == 0:
            # every time the Percent is a multiple of 10 it will
            # wait a little...
            self.DoSomethingElse()
        self.PB.setProgressPercent(self.PB.getProgressPercent()+1)
        if self.go:
            self.parent.after(100, self.DoSomething)

    def DoSomethingElse(self):
        print('Doing something else...')
        self.parent.after(1000, None)

def main():
    root = Tk()
    myapp = Application(root)
    root.mainloop() 

if __name__=='__main__':
    main()
    
