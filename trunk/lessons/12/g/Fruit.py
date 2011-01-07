class Fruit(object):
    __salad = {'quantity': 0} # attributo di classe, vale per tutte le istanze
    # in questo esempio, è un dizionario, di cui ci interessa un solo valore
    # qui lo rendiamo privato

    def __init__(self, name):
        self.setName(name)
        self.__alerts = []
        self.__salad['quantity'] += 1

    def getSaladInfoByKey(self, key):
        return self.__salad[key]

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
    print('Numero di frutti fino ad ora: %d' % myapple.getSaladInfoByKey('quantity'))
     
    myorange= Fruit('arancia siciliana')
    print('Numero di frutti fino ad ora: %d' % myorange.getSaladInfoByKey('quantity'))

    mykiwi= Fruit('kiwi friulano')
    print('Numero di frutti fino ad ora: %d' % mykiwi.getSaladInfoByKey('quantity'))
    
if __name__ == '__main__':
    main()
