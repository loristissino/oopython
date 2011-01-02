customers=[
    ('John', 'Smith', 123, 'p'),
    ('James', 'Baird', 231, 'p'),
    ('Acme SA', None, 458, 'j'),
    ('Diane', 'Kelly', 125, 'p'),
    ('Rebecca', 'Campbell', 457, 'p'),
    ('Alphagamma Ltd', None, 318, 'j'),
    ('Blueskies Inc.', None, 941, 'j')
    ]


def capitalizePersonNames(c):
    if c[3]=='p':
        return ' '.join(c[0:2]).upper()
        # mettiamo in maiuscolo i primi due campi, dopo averli
        # uniti con uno spazio
    else:
        return c[0]
    

names=list(map(capitalizePersonNames, customers))
print(names)

names=list(map(lambda v: v[0] if v[3]=='j' else ' '.join(v[0:2]).upper(), customers))
print(names)




