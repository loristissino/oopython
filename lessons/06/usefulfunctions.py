"""
Questo è un modulo che contiene una funzione che somma tutti i
numeri interi presenti in una lista.

Si noti che la funzione contiene un commento che contiene a sua volta
degli esempi di esecuzione con risultato atteso.

Se si esegue il modulo come codice autonomo i test vengono effettivamente svolti.
"""

def sumup(l):
    """Restituisce la somma di tutti i valori interi di una lista o di una tupla

    Tutti i valori non interi vengono ignorati in silenzio.
    Non è ricorsiva: vengono presi in considerazione solo i valori del primo
    livello della lista (o tupla).

    >>> print(sumup((1,3)))
    4
    >>> print(sumup([12, 20, 40.12, 'foo', 13]))
    45
    """
    
    assert(isinstance(l, (list, tuple)))
    s=0
    for i in l:
        if isinstance(i, int):
            s+=i
    return s

if __name__=='__main__':
    import doctest
    r = doctest.testmod()
    print(r)


