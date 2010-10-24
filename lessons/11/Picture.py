from basic_io import *
from PosInt import *
from Field import *
from Date import *

import collections

class Picture(object):
    nt = collections.namedtuple('fields', 'filename, width, height, filetype, quality, date_taken')

    __fields = nt(
        Field('filename', str, 'nome del file', 30),
        Field('width', PosInt, 'larghezza', 8, 'right'),
        Field('height', PosInt, 'altezza', 8, 'right'),
        Field('filetype', str, 'tipo di file', 5),
        Field('quality', float, 'qualità immagine', 4, 'right'),
        Field('date_taken', Date, 'data di ripresa', 8, 'right')
        )

    __slots__ = nt._fields
        
    def __setattr__(self, name, value):
        assert(isinstance(value, getattr(self.__fields, name).getClassConstraint()))  # non funziona perché name è una stringa, non una classe
        super().__setattr__(name, value)

    def getAttrByName(self, name):
        return self.__getattribute__(name)

    def getAttrByPosition(self, position):
        name = self.__slots__[position]
        return self.getAttrByName(name)

    def inputData(self):
        print("*** INSERIMENTO DATI PER UNA IMMAGINE ***")
        for field in self.__fields:
            self.inputField(field)

    def inputField(self, field):
        message = 'Inserisci un valore per "%s": ' % field.getLabel()
        data=checked_input(message, field.getClassConstraint())
        self.__setattr__(field.getName(), data)

    def outputData(self):
        print('*** DATI DI UNA IMMAGINE ***')
        for field in self.__fields:
            self.outputField(field)

    def outputField(self, field):
        print(field.getLabel() + ': ', self.getAttrByName(field.getName()))

if __name__=="__main__":
    img1=Picture()
    img1.inputData()
    img1.outputData()
    print(img1.getAttrByName('height'))  # funziona
    print(img1.getAttrByPosition(2))  # funziona

