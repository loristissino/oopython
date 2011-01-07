class Fruit(object):

    def __init__(self, name):
        self.setName(name)

    def setName(self, value):
        self.name = value   # name è un attributo pubblico
        return self

    def setQuality(self, value):
        self.__quality = value   # quality è un attributo privato
        return self

    def getName(self):
        return self.name

    def getQuality(self):
        return self.__quality

def main():
    myapple = Fruit('mela granny smith')
    myapple.setQuality(12)
    # equivalente a Fruit.setQuality(myapple, 12)
    print('Nome: %s\nqualità: %d' % (myapple.getName(), myapple.getQuality()))

    # myapple.__quality = 20
    # print(myapple.__quality)

    # L'accesso diretto agli attributi privati è:
    # *) non possibile, se sono stati definiti gli attributi con __slots__
    # *) non raccomandabile, negli altri casi

    # Ad ogni modo, se da fuori si modifica un attributo privato
    # il risultato non è quello che si potrebbe pensare...
    # vedi http://knol.google.com/k/loris-tissino/12-attributi-privati-e-pubblici-di/3s6hcvstzhgkg/43?collectionId=3s6hcvstzhgkg.30&position=12#Uno_o_due_underscore(3F)_(28)piccola_nota_sul_name_mangling(29)
    
    

if __name__ == '__main__':
    main()
