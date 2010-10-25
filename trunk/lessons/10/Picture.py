from basic_io import *
from PosInt import *
import datetime

class Picture():
    __slots__ = ('filename', 'width', 'height', 'filetype', 'quality')

    __classes = {
        'filename': str,
        'width': PosInt,
        'height': PosInt,
        'filetype': str,
        'quality': float,
        'date_taken': int
        }
    

    __fieldlabels = {
        'filename': 'nome del file',
        'width': 'larghezza',
        'height': 'altezza',
        'filetype': 'tipo di file',
        'quality': 'qualità',
        'date_taken': 'data di scatto'
        }
    
    def __init__(self, filename='', width=PosInt(320), height=PosInt(240), filetype='JPEG', quality=1.0):
        # dobbiamo passare i parametri width e height istanziandoli come PosInt
        self.filename = filename
        self.width = width
        self.height = height
        self.filetype = filetype
        self.quality = quality

    def getCompleteDescription(self):
        text = "Immagine \"%s\", larghezza %d, altezza %d" % (
            self.filename,
            self.width,
            self.height
            )
        return text

    def __setattr__(self, name, value):
        assert(isinstance(value, self.__classes[name]))
        super().__setattr__(name, value)

    def inputData(self):
        print("*** INSERIMENTO DATI PER UNA IMMAGINE ***")
        for field in self.__slots__:
            self.inputField(field)

    def inputField(self, field):
        datatype = self.__classes[field]
        message = 'Inserisci un valore per "%s": ' % self.__fieldlabels[field]
        data=checked_input(message, self.__classes[field])
        self.__setattr__(field, data)

if __name__=="__main__":
    img1=Picture()
    img1.inputData()
    print(img1.getCompleteDescription())

