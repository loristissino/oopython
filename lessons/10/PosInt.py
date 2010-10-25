class PosInt(int):
    """Una classe per la rappresentazione di valori interi non negativi"""
    def __init__(self, v):
        try:
            k = int(v)
        except ValueError as err:
            return ValueError
        if k<0:
            raise ValueError


if __name__ == '__main__':
    from basic_io import *
    a=checked_input('inserisci un valore nullo o positivo: ', PosInt)
    print(a)
