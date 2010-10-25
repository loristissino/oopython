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

    def setLabel(self, v):
        self.__label = v
        return self
