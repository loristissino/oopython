import simplemath

"""
Importando il modulo simplemath non vengono eseguite le istruzioni
presenti nel "programma principale"
"""

def circle_area(n):
    return 1

if __name__=='__main__':
    for i in range(0,10):
        print(i, simplemath.circle_area(i))
        print(i, circle_area(i))
