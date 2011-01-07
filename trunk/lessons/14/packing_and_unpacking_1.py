def describe_person(name, age):
    assert(isinstance(name, str))
    assert(isinstance(age, int))
    print('La persona di nome %s ha %d anni' % (name, age))


if __name__=='__main__':
    
    describe_person('mario', 32)
    # chiamata con parametri nel giusto ordine

    describe_person(age=32, name='mario')
    # chiamata con parametri in forma chiave/valore
    # si noti che l'ordine non è importante

    info = ('mario', 32)
    describe_person(*info)
    # chiamata con i parametri in una tupla e "sequence unpacking"

    info = ['mario', 32]
    describe_person(*info)
    # chiamata con i parametri in una lista e "sequence unpacking"

    info = {'age': 32, 'name': 'mario'}
    describe_person(**info)
    # chiamata con i parametri in un dizionario e "dict unpacking"
    # notare che in questo caso si mettono due asterischi
    

    


