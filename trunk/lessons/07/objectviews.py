months={ 'jan': 'Gennaio', 'feb': 'Febbraio', 'mar': 'Marzo' }

print(months)

print(type(months.keys()))
print(type(months.values()))
print(type(months.items()))

keys=months.keys()  # creiamo un riferimento dinamico alle chiavi
keysCopy=tuple(months.keys())  # creiamo una copia delle chiavi esistenti ora

values=months.values() # come sopra, ma per i valori
valuesCopy=tuple(months.values()) # copia dei valori esistenti ora

del months['jan'] # eliminiamo l'elemento con chiave 'jan'

months['apr']='Aprile' # aggiungiamo un elemento con chiave 'apr'

print(keys) # otteniamo la lista aggiornata
print(keysCopy) # otteniamo la copia (non aggiornata)

print(values) # come sopra
print(valuesCopy) # come sopra

