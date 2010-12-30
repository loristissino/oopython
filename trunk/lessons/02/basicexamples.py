"""Un primo esempio di programma Python
In questo esempio vedremo:
- come si scrivono i commenti
- come si formatta l'output
- come si usa la capacità introspettiva del linguaggio
- come si ottiene un input
- come si gestiscono selezioni e cicli
"""

"""I commenti possono essere scritti su una riga a partire dal punto in
cui è presente un #, oppure su più righe (come queste)
"""

print("--------")

amount=50 # assegna il valore 5 alla variabile importo

print(amount)
# visualizza il valore di importo

print("L'importo è ", amount, ".")
# visualizza la costante tra virgolette e poi il valore
# questo tipo di output è sconveniente perché spezza la frase
# (ad esempio, sono difficili le traduzioni)

print("L'importo è %d." % amount)
# visualizza il valore usando una stringa di formattazione
# (%d è un segnaposto per i numeri interi)
# questo tipo di output, simile a quello delle funzioni printf e sprintf del C,
# è deprecato e non sarà più valido in futuro

rate=.073

print("Il tasso è %4.2f%%." % (rate*100))
# la stringa di formattazione è un po' più complicata, perché stiamo
# rappresentando un valore in virgola mobile (segnaposto %f) per il quale
# diciamo quante cifre destinare alla parte dopo la virgola

print("L'importo è %d e il tasso è %4.2f%%." % (amount, rate*100))
# stringa di formattazione con due segnaposto: i valori vanno inseriti in una tupla

print("L'importo è %(amount)s e il tasso è %(rate)s%%." % {"amount": amount, "rate": rate*100})
# stringa di formattazione con uso di segnaposto aventi un nome
# e un dizionario di associazioni per i valori

print("L'importo è {amount} e il tasso è {rate}%.".format(amount=amount, rate=rate*100))
# usando il metodo format della classe str, si possono usare parametri con nome


print(id(amount))
# visualizza il codice univoco associato all'oggetto amount
print(type(amount))
# visualizza il tipo dell'oggetto


name=input("Come ti chiami? ")
print("Ciao, %s." % name)
# per un input da parte dell'utente, è sufficiente usare la funzione input
print(len(name))
# visualizza la lunghezza del nome

age=input("Quanti anni hai? ")
if age.isdigit():
    print("Hai inserito un numero.")
    to100 = 100 - int(age)
    if to100>0:
        print("Ti mancano %d anni per arrivare a 100!" % to100)
else:
    print("Hai inserito qualcosa che non è un numero.")
   


