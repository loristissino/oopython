def do_something(*args):
    print('Elenco degli argomenti:')
    for v in args:
        print(v)
    print('Elenco degli argomenti (con indice numerico):')
    for i in range(len(args)):
        print(i, args[i])

if __name__=='__main__':
    
    do_something('uno', 'due', 'tre')
    

    


