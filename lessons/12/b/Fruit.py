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
    # non possibile, visto che l'attributo è privato

    # print(myapple.__quality)
    # accesso diretto all'attributo
    # non possibile, visto che l'attributo è privato


if __name__ == '__main__':
    main()
