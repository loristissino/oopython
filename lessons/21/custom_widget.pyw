#!/usr/bin/env python3.1

from tkinter import *
from tkinter import messagebox
import fractions

class FractionWidget(object):
    def __init__(self, parent, height=10, width=10, background=None):
        self.parent=parent
        self.height=height
        self.width=width

        self.NumeratorValue=IntVar()
        self.NumeratorValue.set(1)
        self.DenominatorValue=IntVar()
        self.DenominatorValue.set(1)

        vcmd=(self.parent.register(self.doValidation), '%P')
        
        self.MainFrame=Frame(self.parent, width=self.width, height=self.height)
        self.Numerator=Entry(self.MainFrame,
                             textvariable=self.NumeratorValue,
                             width=self.width,
                             justify="right",
                             validate="key",
                             validatecommand=vcmd)
        self.FractionLine=Label(self.MainFrame, text="------")
        self.Denominator=Entry(self.MainFrame,
                               textvariable=self.DenominatorValue,
                               width=self.width,
                               justify="right",
                               validate="key",
                               validatecommand=vcmd)
        self.Numerator.pack(side="top", padx=5, pady=5)
        self.FractionLine.pack(side="top")
        self.Denominator.pack(side="top", padx=5, pady=5)

        if background:
            self.MainFrame['background']=background
        
    
    def doValidation(self, P):
        try:
            k=int(P)
        except ValueError as Err:
            return False
        return True

    def getNumerator(self):
        return self.NumeratorValue.get()
    
    def getDenominator(self):
        return self.DenominatorValue.get()

    def setNumerator(self, value):
        self.NumeratorValue.set(value)
        
    def setDenominator(self, value):
        self.DenominatorValue.set(value)

    def __setitem__(self, key, value):
        if key in ('background', 'bg', 'borderwidth', 'bd', 'relief'):
            self.MainFrame[key]=value
        if key=='numerator':
            self.setNumerator(value)
        if key=='denominator':
            self.setDenominator(value)

    def __getitem__(self, key):
        if key in ('background', 'bg', 'borderwidth', 'bd', 'relief'):
            return self.MainFrame[key]
        if key=='numerator':
            return self.getNumerator()
        if key=='denominator':
            return self.getDenominator()
            
    def pack(self, *args, **kwargs):
        self.MainFrame.pack(*args, **kwargs)

    def grid(self, *args, **kwargs):
        self.MainFrame.grid(*args, **kwargs)
        
    def place(self, *args, **kwargs):
        self.MainFrame.place(*args, **kwargs)


class Application(object):
    def __init__(self, parent):
        
        self.parent = parent

        self.Fraction=FractionWidget(self.parent, background='red')
        self.Fraction['borderwidth']=10
        self.Fraction['relief']='ridge'
        # i valori possibili per relief sono
        # 'sunken', 'raised', 'groove', 'ridge'
        self.Fraction['numerator']=12
        self.Fraction['denominator']=24

        self.Fraction.pack({'side':'top', 'padx':10, 'pady':10})

        self.SimplifyButton=Button(
            self.parent,
            text="Semplifica",
            command=self.SimplifyButton_Click
            )
        self.SimplifyButton.pack({'side':'top', 'padx':10, 'pady':10})

    def SimplifyButton_Click(self):
        if self.Fraction.getDenominator()==0:
            messagebox.showinfo(message='Non è ammesso il denominatore zero.')
        f=fractions.Fraction(self.Fraction['numerator'], self.Fraction.getDenominator())
        # si può accedere ai valori sia con le parentesi quadre sia con il metodo specifico
        self.Fraction.setNumerator(f.numerator)
        self.Fraction.setDenominator(f.denominator)
        

def main():
    root = Tk()
    myapp = Application(root)
    root.mainloop() 

if __name__=='__main__':
    main()
    
