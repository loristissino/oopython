import math

def input_number(message, accept_float=False):
    """Permette l'inserimento di un numero in maniera controllata.

    Chiede in input una stringa usando *message* come prompt, poi
    tenta la conversione in numero e restituisce il numero
    convertito. Se viene inserito un valore che non è un numero,
    viene richiesto di nuovo l'inserimento.
    Se *accept_float* è vero, accetta anche numeri in virgola mobile.
    """
    while(True):
        v=input(message)
        try:
            if accept_float:
                n=float(v)
            else:
                n=int(v)
            return n
        except ValueError as err:
            print("Sembra che tu non abbia inserito un numero valido…")


def circle_area(radius):
    """Restituisce l'area di un cerchio, dato il raggio *radius*.

    >>> print(circle_area(12))
    452.389342117
    >>> print(circle_area(12.3))
    475.291552562
    """

    assert(isinstance(radius, (int, float)))
    return radius ** 2 * math.pi


if __name__=="__main__":
    r=input_number("Inserisci il raggio del cerchio: ")
    a=circle_area(r)
    print("L'area di un cerchio di raggio %f è %f." % (r, a))
