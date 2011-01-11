class Fruit(object):
    __salad = 0

    @classmethod
    def __incSaladCount(cls):
        cls.__salad += 1

    @classmethod
    def getSaladCount(cls):
        return cls.__salad

    __slots__ = ('name', '__alerts', '__quality')
    
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


    def getQuality(self):
        try:
            return self.__quality
        except AttributeError as err:
            return None
        # visto che è una proprietà cancellabile, dobbiamo inserire il codice
        # in un try... except
    
    def setQuality(self, value):
        if 0 <= value <= 100: 
            self.__quality = value
        else:
            self.__quality = 50
            self.__addAlert('bad quality: %d' % value)

    def delQuality(self):
        print('removing quality')
        del self.__quality

    quality=property(
        getQuality,
        setQuality,
        delQuality,
        'Quality of the picture. Can be any value between 0 and 100 (included).'
        )



    @property
    def is_good(self):
        if self.quality:
            return self.quality > 70

def main():
    myapple = Fruit('mela granny smith') 
    myapple.quality = 10
    print(myapple.quality, myapple.is_good)
    myapple.quality = 75
    print(myapple.quality, myapple.is_good)
    del myapple.quality
    print(myapple.quality, myapple.is_good)

    print(Fruit.quality.__doc__)

    # myapple.is_good = False
    # non funziona (manca il setter)
    
if __name__ == '__main__':
    main()
