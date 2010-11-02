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

    def __str__(self):
        return self.getName()

    def getName(self):
        return self.name

    def setName(self, value):
        self.name = value
        return self

    def __addAlert(self, value):
        self.__alerts.append(value)
        return self

    def getName(self):
        return self.name

    def getAlerts(self):
        return self.__alerts

    @property
    def quality(self):
        return self.__quality
    
    @quality.setter
    def quality(self, value):
        if 0 <= value <= 100: 
            self.__quality = value
        else:
            self.__quality = 50
            self.__addAlert('bad quality: %d' % value)

def main():
    myapple = Fruit('mela granny smith')
    myapple.quality = 10
    print('quality %d' % myapple.quality)
    print('Allarmi: ', *myapple.getAlerts())
    myapple.quality = -20

    
    print('quality %d' % myapple.quality)
    print('Allarmi: ', *myapple.getAlerts())
    
if __name__ == '__main__':
    main()
