from Picture import *

class PictureBox(list):
    def showPictures(self):
        for i in range(len(self)):
            print(self[i].getCompleteDescription())        

if __name__=='__main__':
    mybox=PictureBox()

    n = checked_input("Quante immagini vuoi inserire? ", int)

    for i in range(n):
        pic=Picture()
        pic.inputData()
        mybox.append(pic)

    mybox.showPictures()
