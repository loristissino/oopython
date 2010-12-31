class Picture():

    def __init__(self, filename, width=320, height=240, filetype='JPEG'):
        self.filename = filename
        self.setWidth(width)
        self.setHeight(height)
        self.filetype=filetype

    def setWidth(self, value):
        assert(isinstance(value, int))
        assert(value>=0)
        self.__width = value
        return self

    def setHeight(self, value):
        assert(isinstance(value, int))
        assert(value>=0)
        self.__height = value
        return self

    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height

    def getCompleteDescription(self):
        text = "Immagine %s, larghezza %d, altezza %d" % (
            self.filename,
            self.getWidth(),
            self.getHeight()
            )
        return text
    

img1=Picture('gatto.jpg', height=480)

img1.setWidth(2000).setHeight(3000)
img1.__width = -10 # crea un nuovo attributo, non fa accedere a quello privato

print("Visualizzazione dell'intero dizionario:")
print(img1.__dict__)

print(img1.getCompleteDescription())
