import usefulfunctions

def countdown(n, k=100, step=1):
    '''Restituisce una lista di *n* valori interi, decrementando a partire da *k*'''
    l=[]
    for i in range(n):
        l.append(k-i*step)
    return l
        

if __name__=='__main__':
    n=countdown(10,250, 3)
    print(n)
    print('La somma è %d.' % sumup(n))
    
