a = ['arancia', 'mela', 'pera', 'fragola', 'banana', 'ananas']

primo, secondo, *altri = a

print('primo:    ', primo)
print('secondo:  ', secondo)
print('altri:    ', altri)

primo, *centrali, ultimo = a

print('primo:    ', primo)
print('centrali: ', centrali)
print('ultimo:   ', ultimo)


nome="Mario"
primalettera,*successive = nome

print('prima lettera: ', primalettera)
print('successive:    ', successive)

