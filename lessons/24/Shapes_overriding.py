import math

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

class Circle(Shape):
    def __init__(self, radius):
        self._radius=radius

    @property
    def perimeter(self):
        return self._radius*math.pi*2

    @property
    def area(self):
        return math.pi * self._radius ** 2

    def place(self, x, y):
        super().place(x, y)
        self._center=(self._x+self._radius, self._y+self._radius)


if __name__=='__main__':
    c=Circle(4)
    c.place(-1,12)
    print('Centro del cerchio:', c.center)

    r=Rectangle(10,20)
    r.place(4,-2)
    print('Centro del rettangolo:', r.center)
