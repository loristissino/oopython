"""
See http://tinyurl.com/oopython
"""

from Picture import *

class PictureBox(list):
    def showHeader(self):
        fields=list()
        # creiamo una lista dove mettere le etichette dei campi
        for field in Picture.getFields():
            fields.append(field.getLabel())
            # aggiungiamo un'etichetta alla lista
        print(*fields, sep=' | ')
        # visualizziamo tutte le etichette della lista
        # *fields trasforma l'oggetto fields in un elenco, come se
        # scrivessimo
        # print(fields[0], fields[1], fields[2], ...)
        
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

