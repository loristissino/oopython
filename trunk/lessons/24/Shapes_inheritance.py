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


class Circle(Shape):
    def __init__(self, radius):
        self._radius=radius

    @property
    def perimeter(self):
        return self._radius*math.pi*2

    @property
    def area(self):
        return math.pi * self._radius ** 2



if __name__=='__main__':
    c=Circle(4)
    print('Area del cerchio:', c.area)
    print('Perimetro del cerchio:', c.perimeter)
    print('Nome:', c.name)
    print(type(c))

    r=Rectangle(10,20)
    print('Area del rettangolo:', r.area)
    print('Perimetro del rettangolo:', r.perimeter)
    print('Nome:', r.name)
    print(type(r))
    
    shapes=[
        Circle(5),
        Rectangle(9,10),
        Rectangle(11,21,'R1'),
        ]
    for s in shapes:
        print('----')
        print(s.name, s.area)
        # se dobbiamo mostrare più proprietà possiamo farlo così:
        for p in ('name', 'area', 'perimeter'):
            print(p,':',getattr(s,p))

