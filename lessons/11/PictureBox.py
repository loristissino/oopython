"""
See http://tinyurl.com/oopython
"""

from Picture import *

class PictureBox(list):
    def showHeader(self):
        for field in Picture.getFields(Picture):
            print(field.getLabel())
    def showPictures(self):
        for i in range(len(self)):
            self[i].outputData()
            

if __name__=='__main__':
    mybox=PictureBox()

    n = checked_input("Quante immagini vuoi inserire? ", int)

    for i in range(n):
        pic=Picture()
        pic.inputData()
        mybox.append(pic)

    mybox.showHeader()
    mybox.showPictures()

