"""
See http://tinyurl.com/oopython
"""

class PosInt(int):
    """Una classe per la rappresentazione di valori interi positivi"""
    def __init__(self, v):
        try:
            self = int(v)
        except ValueError as err:
            return ValueError
        if self<=0:
            raise ValueError


if __name__ == '__main__':
    from basic_io import *
    a=checked_input('inserisci un valore positivo: ', PosInt)
    print(a, type(a))

    n=PosInt(12)
    print(dir(n))
    
