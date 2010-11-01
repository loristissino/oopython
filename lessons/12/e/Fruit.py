class Fruit(object):
    salad = [] # attributo di classe, vale per tutte le istanze
    # in questo esempio, è una lista di tutti i frutti istanziati

    def __init__(self, name):
        self.setName(name)
        self.__alerts = []
        self.salad.append(self)

    def __str__(self):
        return self.getName()

    def getName(self):
        return self.name

    def setName(self, value):
        self.name = value
        return self

    def getIdx(self):
        return self.__idx

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

    def getName(self):
        return self.name

    def getQuality(self):
        return self.__quality

    def getAlerts(self):
        return self.__alerts

def main():
    myapple = Fruit('mela granny smith')
    print('macedonia a cui appartiene la mela:') 
    print(*myapple.salad, sep=", ")
    
    myorange= Fruit('arancia siciliana')
    print('macedonia a cui appartiene l\'arancia:') 
    print(*myorange.salad, sep=", ")

    mykiwi= Fruit('kiwi friulano')
    print('macedonia a cui appartiene il kiwi:') 
    print(*mykiwi.salad, sep=", ")

    print('==========')    
    print('macedonia a cui appartiene la mela:') 
    print(*myapple.salad, sep=", ")
    print('macedonia a cui appartiene l\'arancia:') 
    print(*myorange.salad, sep=", ")
    print('macedonia a cui appartiene il kiwi:') 
    print(*mykiwi.salad, sep=", ")

    
if __name__ == '__main__':
    main()
