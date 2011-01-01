VALUES = 10
MAX = 1000

import random

def mysort(v):
    for i in range(len(v)-1):
        for j in range(i,len(v)):
            if v[i] > v[j]:
                v[i],v[j] = v[j], v[i]


k1=random.sample(range(MAX), VALUES) # creiamo una lista di valori casuali
k2=k1[:] # copiamo l'intera lista

mysort(k1) # chiamiamo la nostra funzione
print(k1)  # visualizziamo la lista ordinata
k2.sort()  # chiamiamo la funzione standard
print(k2)  # visualizziamo la lista ordinata
print(k1==k2) # controlliamo che il nostro ordinamento sia corretto
# notare che si possono confrontare due liste con una sola istruzione
