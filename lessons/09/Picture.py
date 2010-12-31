from basic_io import *

class Picture():
    __slots__ = ('filename', 'width', 'height', 'filetype', 'quality')
    # __slots__ è una parola chiave che definisce l'elenco degli attributi 
    # di una classe in modo vincolante

    __attributeTypes = {
        'filename': str,
        'width': int,
        'height': int,
        'filetype': str,
        'quality': float
        }
    # __attribuiteTypes è un dizionario privato in cui memorizzo i tipi
    # associati a ciascun attributo

    __attributeLabels = {
        'filename': 'nome del file',
        'width': 'larghezza',
        'height': 'altezza',
        'filetype': 'tipo di file',
        'quality': 'qualità'
        }
    # __attributeLabels è un dizionario privato in cui memorizzo i tipi
    # associati a ciascun attributo

    # costruttore
    def __init__(self, filename='', width=320, height=240, filetype='JPEG', quality=1.0):
        self.filename = filename
        self.width = width
        self.height = height
        self.filetype = filetype
        self.quality = quality

    def getCompleteDescription(self):
        """Return a complete description of the picture as a string
        filled with all attributes' names and values.
        """
        fields=[]
        for attrName in self.__slots__:
            DisplayName = str(self.__attributeLabels[attrName])
            AttributeValue= str(getattr(self, attrName))
            # il metodo getattr serve per accedere al valore di un
            # attributo avendo il suo nome
            # getattr(self, 'width') corrisponde a self.width
            fields.append('%s: %s' % (DisplayName, AttributeValue))
        return ', '.join(fields)
        # il metodo join applicato ad una stringa fa sì che la stringa
        # venga usata come "collante" per unire tutti gli elementi della
        # lista che ha come argomento

    def __setattr__(self, name, value):
        assert(isinstance(value, self.__attributeTypes[name]))
        super().__setattr__(name, value)

    def inputFields(self):
        print("*** INSERIMENTO DATI PER UNA IMMAGINE ***")
        for field in self.__slots__:
            self.inputField(field)

    def inputField(self, field):
        datatype = self.__attributeTypes[field]
        message = 'Inserisci un valore per "%s": ' % self.__attributeLabels[field]
        data=checked_input(message, datatype)
        self.__setattr__(field, data)

    def showFields(self):
        print("*** VISUALIZZAZIONE DATI PER UNA IMMAGINE ***")
        for attrName in self.__slots__:
            self.showField(attrName)

    def showField(self, attrName):
        '''Prints out a list of field names and values'''
        print('%s --> %s' % (
            self.__attributeLabels[attrName],
            str(getattr(self, attrName))
            ))
        

if __name__=="__main__":
    img1=Picture()
    img1.inputFields()
    print(img1.getCompleteDescription())
    img1.showFields()
    

