#!/usr/bin/env python3.1

import pickle

data=('foo', 'bar', 'baz')

with open('mydata', 'wb') as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

data=()

with open('mydata', 'rb') as f:
    data = pickle.load(f)

print(data)

