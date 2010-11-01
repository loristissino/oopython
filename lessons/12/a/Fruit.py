class Fruit(object):

    def __init__(self, name):
        self.setName(name)

    def setName(self, value):
        self.name = value   # name è un attributo pubblico
        return self

    def setQuality(self, value):
        self.quality = value   # quality è un attributo pubblico
        return self

    def getName(self):
        return self.name

    def getQuality(self):
        return self.quality

def main():
    myapple = Fruit('mela granny smith')
    myapple.setQuality(12)
    # equivalente a Fruit.setQuality(myapple, 12)
    print('Nome: %s\nqualità: %d' % (myapple.getName(), myapple.getQuality()))

    myapple.quality = 20
    print('Nome: %s\nqualità: %d' % (myapple.getName(), myapple.getQuality()))
    # accesso agli attributi tramite funzione "getter"

    print(myapple.quality)
    # accessodiretto all'attributo

    myorange = Fruit('arancia siciliana')
    myorange.quality = -20
    # non viene fatto nessun controllo sul valore impostato...
    print('Nome: %s\nqualità: %d' % (myorange.getName(), myorange.getQuality()))
    
    

if __name__ == '__main__':
    main()
