print("*** Ciclo while...")
n=2
while(n<5):
    print(n)
    n+=1 # incremento della variabile n di una unità
print("ciclo while finito...")


# se vogliamo un test in coda (come nel repeat... until del pascal)
# possiamo usare la parola chiave break
n=2
print("*** Ciclo con break condizionato")
while(True):
    print(n)
    n+=1
    if(n>=5):
        break
print("fine ciclo con break condizionato")

       
# I cicli for si basano su oggetti che possono essere iterati:
print("*** Ciclo for basato su oggetti iterabili")

fruits=["arancia", "mela", "pera", "ananas"]
for fruit in fruits:
    print(fruit)

print("*** Ciclo for basato su diversi oggetti iterabili percorsi in parallelo")
colors=["arancio", "bianco", "bianco", "giallo"]
for fruit, color in zip(fruits, colors):
    print('Il frutto %s ha la polpa color %s.' % (fruit, color))

print("*** Ciclo for basato su oggetti iterabili")
sentence="ma che bel castello marcondirodirondello..."
for letter in sentence:
    if letter in "aeiou":
        print(letter.upper(), end="") # mettiamo in maiuscolo le vocali...
    else:
        print(letter, end="")
print()

# cicli con indici numerici:
print("*** Ciclo for su range(5)")
for i in range(5):
    print(i)

print("*** Ciclo for su range(5, 10)")
for i in range(5,10):
    print(i)

print("*** Ciclo for su range(10, 20, 2)")
for i in range(10, 20, 2):
    print(i)

print("*** Ciclo for su range(5, 0, -1)")
for i in range(5,0,-1):
  print(i)

print("*** Ciclo for per i caratteri di una stringa alla rovescia")
name="Mario"
for i in range(len(name)-1,-1,-1):
  print(name[i])

print("*** Alternativa per visualizzare i caratteri di una stringa alla rovescia")
name="Mario"
for i in range(1,len(name)+1): # ciclo da 1 alla lunghezza della stringa +1
  print(-i, name[-i]) # uso l'opposto di i

