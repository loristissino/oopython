class Foo():
    def __init__(self):
        self.bar = 1
        self._bar = 2
        self.__bar = 3

f = Foo()
print("f.bar: %d" % f.bar)
print("f._bar: %d" % f._bar)
#print("f.__bar: %d" % f.__bar)

print(f.__dict__)
print("f.__bar (accesso indiretto): %d" % f.__dict__['_Foo__bar'])
print("f.__bar (accesso con nome della classe): %d" % f._Foo__bar)


