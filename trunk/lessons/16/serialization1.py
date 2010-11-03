#!/usr/bin/env python3.1

import pickle

data=('foo', 'bar', 'baz')

f = open('mydata', 'wb')
pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
f.close()

data=()

f = open('mydata', 'rb')
data = pickle.load(f)
f.close()

print(data)

class Foo():
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Foo «%s»' % self.name

data = (
    Foo('abc'), Foo('def'), Foo('ghi'),
    ['uno', 'due', 'tre'],
    {'a': 'primo', 'b': 'secondo', 'c': 'terzo'}
    )

f = open('mydata', 'wb')
pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
f.close()

data=()

f = open('mydata', 'rb')
data = pickle.load(f)
f.close()

print(data)
print(data[0])
