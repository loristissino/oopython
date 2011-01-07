class Fruit(object):
    __salad = 0

    @classmethod
    def __incSaladCount(cls):
        cls.__salad += 1

    @classmethod
    def getSaladCount(cls):
        return cls.__salad

    def __init__(self, name):
        self.setName(name)
        self.__alerts = []
        self.__incSaladCount()

    def getName(self):
        return self.name

    def setName(self, value):
        self.name = value
        return self

    def setQuality(self, value):
        if 0 <= value <= 100: 
            self.__quality = value
        else:
            self.__quality = 50
            self.__addAlert('bad quality: %d' % value)
        return self

    def __addAlert(self, value):
        self.__alerts.append(value)
        return self

    def getQuality(self):
        return self.__quality

    def getAlerts(self):
        return self.__alerts

def main():
    myapple = Fruit('mela granny smith')
    print('Numero di frutti fino ad ora: %d' % myapple.getSaladCount())
     
    myorange= Fruit('arancia siciliana')
    print('Numero di frutti fino ad ora: %d' % myorange.getSaladCount())

    mykiwi= Fruit('kiwi friulano')
    print('Numero di frutti fino ad ora: %d' % mykiwi.getSaladCount())
    print('Numero di frutti fino ad ora: %d' % myapple.getSaladCount())
    print('Numero di frutti fino ad ora: %d' % Fruit.getSaladCount())
    
if __name__ == '__main__':
    main()
