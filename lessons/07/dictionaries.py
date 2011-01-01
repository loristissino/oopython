months={ 'jan': 'Gennaio', 'feb': 'Febbraio', 'mar': 'Marzo' }

print(months)

months['apr'] = 'Aprile'
months['may'] = 'Maggio'
months['june'] = 'Giugno'

print(months)

print('\nChiavi:')
for key in months.keys():
    print(key)

print('\nValori:')
for value in months.values():
    print(value)


print('\nChiavi e valori:')
for key, value in months.items():
    print(key, ' --> ', value)

weekdays=dict(zip(
    ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'),
    ('Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica')
    ))

print(weekdays)
