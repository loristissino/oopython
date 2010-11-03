class Foo():
    def __init__(self):
        self.bar = 1
        self._bar = 2
        self.__bar = 3

class DerivedFromFoo(Foo):
    def update(self):
        self.bar = 10
        self._bar = 20
        self.__bar = 30

f = DerivedFromFoo()
print(f.__dict__)

f.update()
print(f.__dict__)

