from basic_io import *
from PosInt import *
from Field import *
from Date import *

import collections

class Picture(object):
    nt = collections.namedtuple('fields', 'filename, width, height, filetype, quality, date_taken')

    __fields = nt(
        Field(str, 'nome del file', 30),
        Field(PosInt, 'larghezza', 8, 'right'),
        Field(PosInt, 'altezza', 8, 'right'),
        Field(str, 'tipo di file', 5),
        Field(float, 'qualità immagine', 4, 'right'),
        Field(Date, 'data di ripresa', 8, 'right')
        )

    __slots__ = nt._fields
        
    def __setattr__(self, name, value):
        assert(isinstance(value, getattr(self.__fields, name).getClassConstraint()))
        super().__setattr__(name, value)

    def getAttrByName(self, name):
        return self.__getattribute__(name)

    def getAttrByPosition(self, position):
        name = self.__slots__[position]
        return self.getAttrByName(name)

    def inputData(self):
        print("*** INSERIMENTO DATI PER UNA IMMAGINE ***")
        for fieldname, field in zip(self.__slots__, self.__fields):
            self.inputField(fieldname, field)

    def inputField(self, fieldname, field):
        message = 'Inserisci un valore per "%s": ' % field.getLabel()
        data=checked_input(message, field.getClassConstraint())
        self.__setattr__(fieldname, data)

    def outputData(self):
        print('*** DATI DI UNA IMMAGINE ***')
        for fieldname, field in zip(self.__slots__, self.__fields):
            self.outputField(fieldname, field)

    def outputField(self, fieldname, field):
        print(field.getLabel(),': ', self.getAttrByName(fieldname))

if __name__=="__main__":
    img1=Picture()
    img1.inputData()
    img1.outputData()
    print(img1.getAttrByName('height'))
    print(img1.getAttrByPosition(2))

