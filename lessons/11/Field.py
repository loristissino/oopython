"""
See http://tinyurl.com/oopython
"""

class Field():
    def __init__(self, class_constraint, label='',  size=20, alignment='left'):
        self.__class_constraint = class_constraint
        self.__label = label
        self.__size = size
        self.__alignment = alignment

    def getClassConstraint(self):
        return self.__class_constraint
    def getLabel(self):
        return self.__label
    def getSize(self):
        return self.__size
    def getAlignment(self):
        return self.__alignment
    def getMethod(self):
        return self.__method
        # il metodo della classe self.__class_constraint da usare
        # per la convalida dei dati (se necessario)
        # (giusto un esempio per far capire che se si vuole si possono
        # aggiungere altri campi per fronteggiare nuove necessità)

    def setLabel(self, v):
        self.__label = v
        return self

    # gli altri metodi vanno implementati...
