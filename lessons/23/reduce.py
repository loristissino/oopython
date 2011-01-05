import functools
import operator

ages=(22, 24, 21)

print('--- Calcolo somma età con functools.reduce (e funzione lambda) ---')
total_age=functools.reduce(lambda x, y: x+y, ages)
print(total_age)

print('--- Calcolo somma età con functools.reduce (e operator.add) ---')

total_age=functools.reduce(operator.add, ages)
print(total_age)


people=(
    ('Alice', 22),
    ('Bob', 24),
    ('Charlie', 21)
    )


print('--- Calcolo somma età da una serie di tuple con apposita funzione ---')

def sumUp(a,b):
    # sommma al valore corrente (a) il secondo elemento della tupla b 
    return a+b[1]

total_age=functools.reduce(sumUp, people, 0)
# si noti che in questo caso bisogna inizializzare il sommatore (altrimenti viene
# preso il primo valore, che è una tupla
print(total_age)

print('--- Calcolo somma età da una serie di tuple con funzione lambda ---')
total_age=functools.reduce(lambda x, y: x+y[1], people, 0)
print(total_age)

values=(10,8,8,9,4)
weights=(1,1,2,3,2)

print('--- Calcolo di una media ponderata in maniera tradizionale ---')
ps=0 # somma dei prodotti
ws=0 # somma dei pesi

for v, w in zip(values, weights):
    ps+=v*w
    ws+=w
    
weighted_average = ps/ws
print(weighted_average)

print('--- Calcolo di una media ponderata con functools.reduce ---')
weighted_average = functools.reduce(operator.add, map(operator.mul, values, weights), 0)/functools.reduce(operator.add, weights)
print(weighted_average)

