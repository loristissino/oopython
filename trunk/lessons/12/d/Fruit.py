class Fruit(object):

    def __init__(self, name):
        self.setName(name)
        self.__alerts = [] # un attributo privato (lista degli allarmi)

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

    def getName(self):
        return self.name

    def getQuality(self):
        return self.__quality

    def getAlerts(self):
        return self.__alerts

def main():
    myapple = Fruit('mela granny smith')
    myapple.setQuality(12)
    print('Nome: %s\nqualità: %d' % (myapple.getName(), myapple.getQuality()))

    myapple.setQuality(-10)
    # impostiamo un valore fuori dal range valido
    print('Nome: %s\nqualità: %d' % (myapple.getName(), myapple.getQuality()))
    # ... e vediamo che viene impostato a 50
    print("Lista degli allarmi: ", myapple.getAlerts())

if __name__ == '__main__':
    main()
