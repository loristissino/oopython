from Picture import *

class PictureBox(list):
    def showPictures(self):
        for i in range(len(self)):
            # NB len(self) ha senso in questo caso, visto che self è una lista
            if isinstance(self[i], Picture):
                # controlliamo, potrebbe essere None
                print(self[i].getCompleteDescription())

    def append(self, item):
        # ridefinizione del metodo append (se si vuole essere sicuri che non
        # si possano aggiungere elementi non di tipo Picture)
        assert(isinstance(item, Picture))
        super().append(item) # uso il metodo della classe padre

    def insert(self, position, item):
        # ridefinizione del metodo insert (se si vuole essere sicuri che non
        # si possano aggiungere elementi non di tipo Picture)
        assert(isinstance(item, Picture))
        super().insert(position, item) # uso il metodo della classe padre       

    def __setitem__(self, key, value):
        # ridefinizione del metodo __setitem__ (se si vuole essere sicuri che non
        # si possano cambiare elementi con oggetti non di tipo Picture, a meno
        # che non li si imposti a None, che invece consideriamo cosa lecita)
        assert(value is None or isinstance(value, Picture))
        super().__setitem__(key, value) # uso il metodo della classe padre
        

if __name__=='__main__':
    mybox=PictureBox()

    n = checked_input("Quante immagini vuoi inserire? ", int)

    for i in range(n):
        pic=Picture()
        pic.inputFields()
        mybox.append(pic)   

    mybox.showPictures()
