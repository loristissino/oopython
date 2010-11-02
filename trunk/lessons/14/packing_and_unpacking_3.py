def do_something(*args, **kwargs):
    print('Elenco degli argomenti senza parola chiave:')
    print(args)
    for v in args:
        print(v)
    print('Elenco degli argomenti con parola chiave:')
    print(kwargs)
    for k,v in kwargs.items():
        print(k, '=', v)

if __name__=='__main__':

    do_something('uno', 'due', 'tre', valore=100, totale=200)
    

    


