def checked_input(message, constraint_class):
    """Permette l'inserimento di un valore in maniera controllata.

    Chiede in input una stringa usando *message* come prompt, poi
    tenta la conversione nella classe *constraint_class* e
    restituisce il valore convertito.
    Se viene inserito un valore non valido, viene richiesto di
    nuovo l'inserimento.
    """
    while(True):
        v=input(message)
        try:
            n = constraint_class(v)
            return n
        except ValueError as err:
            print("Sembra che tu non abbia inserito un valore valido…")

