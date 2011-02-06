import math
from datetime import datetime

class Shape(object):
    '''Un oggetto di tipo Shape rappresenta una figura geometrica generica'''

    @property
    def area(self):
        '''Restituisce l'area della figura'''
        pass

    @property
    def perimeter(self):
        '''Restituisce il perimetro della figura'''
        pass

    @property
    def name(self):
        return getattr(self, '_name', 'Untitled')
        # restituisce l'attributo _name se esiste, altrimenti 'Untitled'

    def place(self, x, y):
        '''Imposta le coordinate dell'estremo NW della figura'''
        self._x=x
        self._y=y

    @property
    def center(self):
        '''Restituisce la tupla di coordinate del centro della figura'''
        return self._center

class Rectangle(Shape):
    def __init__(self, width, height, name="A rectangle"):
        self._width=width
        self._height=height
        self._name=name

    @property
    def perimeter(self):
        return 2*(self._height+self._width)

    @property
    def area(self):
        return self._height * self._width

    def place(self, x, y):
        super().place(x, y)
        self._center=(self._x+self._width/2, self._y+self._height/2)

    def setName(self, value):
        self._rname=value

class Logged(object):
    def __init__(self, path):
        self._path=path

    def startlogger(self):
        self._file=open(self._path, 'a')

    def stoplogger(self):
        self._file.close()

    def write(self, line):
        if not line.endswith('\n'):
            line+='\n'
        output = '(%d) %s: %s' % (id(self), str(datetime.now()), line)
        self._file.write(output)

    def setName(self, value):
        self._lname=value


class LoggedRectangle(Rectangle, Logged):
    def __init__(self, width, height, path, name="A logged rectangle"):
        Rectangle.__init__(self, width, height, name)
        Logged.__init__(self, path)

    def place(self, x, y):
        super().place(x, y)
        self.write('Placed in (%f, %f) position.' %(x,y))
        
    def printName(self):
        print(getattr(self, '_rname', 'rname missing'))
        print(getattr(self, '_lname', 'lname missing'))
    
if __name__=='__main__':
    lr=LoggedRectangle(20, 30, '/tmp/rlog', 'MyRect')
    lr.startlogger()
    lr.write('Object "%s" with area %f has been created.' % (lr.name, lr.area))
    lr.place(-15,12)
    lr.stoplogger()

    lr.setName('Foo')
    lr.printName()


    l=Logged('/tmp/llog')
    l.startlogger()
    l.write('creato oggetto')
    l.name='Foo'
    l.write('assegnato nome a oggetto')
    l.stoplogger()






print(LoggedRectangle.__mro__)

