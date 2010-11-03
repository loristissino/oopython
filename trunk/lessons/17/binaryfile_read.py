import struct

class Person():
    struct_format = struct.Struct('<20sb')

    def __init__(self, name, age):
        self.name = name.strip('\0x00 ')
        self.age = age

    def getPacked(self):
        return self.struct_format.pack(
            self.name.encode('UTF-8'),
            self.age
            )

    def __str__(self):
        return 'Nome: %s, età: %d' % (self.name, self.age)

with open('people.dat', 'rb') as f:
    while True:
        data = f.read(Person.struct_format.size)
        if not data:
            break
        name, age = Person.struct_format.unpack(data)
        p = Person(name.decode('UTF-8'), age)
        print(p)
        
        




