import struct

class Person():
    struct_format = struct.Struct('<20sb')

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getPacked(self):
        return self.struct_format.pack(
            self.name.encode('UTF-8'),
            self.age
            )

people = (
    Person('Mario Rossi', 20),
    Person('Alberto Alberti', 21),
    Person('Barbara Balducci', 22),
    Person('Carla Carletti', 23)
    )

with open('people.dat', 'wb') as f:
    for person in people:
        f.write(person.getPacked())


