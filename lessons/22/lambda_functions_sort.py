def showList(l):
    for i in l:
        print(i)
        

def surname_first(data):
    return (data[1], data[0], data[2])

def code_first(data):
    return (data[2], data[1], data[0])

people=[
    ('John', 'Smith', 123),
    ('James', 'Baird', 231),
    ('Rebecca', 'Campbell', 457),
    ('Diane', 'Kelly', 125)
    ]

print('*** ordinamento per nome ***')
people.sort()
showList(people)
print('*** ordinamento per cognome ***')
people.sort(key=surname_first)
showList(people)
print('*** ordinamento per codice ***')
people.sort(key=code_first)
showList(people)

print('*** ordinamento per cognome con funzione lambda ***')
people.sort(key=lambda x: (x[1], x[0], x[2]))
showList(people)

print('*** ordinamento per codice con funzione lambda ***')
people.sort(key=lambda x: (x[2], x[1], x[0]))
showList(people)


k=int(input("In base a quale campo vuoi l'ordinamento? "))
print('*** ordinamento su campo a scelta ***')
if not 0<k<3: k=0
people.sort(key=lambda x: x[k])
showList(people)



customers=[
    ('John', 'Smith', 123, 'p'),
    ('James', 'Baird', 231, 'p'),
    ('Acme SA', None, 458, 'j'),
    ('Diane', 'Kelly', 125, 'p'),
    ('Rebecca', 'Campbell', 457, 'p'),
    ('Alphagamma Ltd', None, 318, 'j'),
    ('Blueskies Inc.', None, 941, 'j')
    ]

customers.sort(key=lambda x: x[0] if x[3]=='j' else x[1])

print('*** ordinamento per nome o cognome con funzione lambda e selezione ***')
showList(customers)

