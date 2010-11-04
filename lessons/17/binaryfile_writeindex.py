import struct

index_format = struct.Struct('<h')

with open('people.idx', 'wb') as f:
    for idx in (3,1,0,2):
        f.write(fmt.pack(idx))



