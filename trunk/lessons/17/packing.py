import struct

FORMAT='<2hf'
data = struct.pack(FORMAT, 30000, -12, 2.35)  #packing
items = struct.unpack(FORMAT, data)  #unpacking
print(items)


name="Mario Rossi Albertucci"
age=20
FORMAT='<20sb'
data = struct.pack(FORMAT, name.encode('UTF-8'), age)  #packing
items = struct.unpack(FORMAT, data)  #unpacking
print(items[0].decode('UTF-8'), items[1])




# http://docs.python.org/py3k/library/struct.html
