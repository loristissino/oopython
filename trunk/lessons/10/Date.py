"""
See http://tinyurl.com/oopython
"""

from datetime import *

class Date():
    def __init__(self, value):
        self.__date=datetime.strptime(value, "%d/%m/%Y")
    def getYear(self):
        return self.__date.year
    def getMonth(self):
        return self.__date.month
    def getDay(self):
        return self.__date.day
    def __str__(self):
        return self.__date.strftime("%d/%m/%Y")

print("Esempio con classe wrapper (1)")    
n=Date('20/10/2010')
print(n, type(n))
print(n.getYear())


class Date():
    def __init__(self, value):
        self.__date=datetime.strptime(value, "%d/%m/%Y")
    def __getattr__(self, name):
        return getattr(self.__date, name)
    def __str__(self):
        return self.__date.strftime("%d/%m/%Y")

print("Esempio con classe wrapper (2)")    
n=Date('20/10/2010')
print(n, type(n))
print(n.year)



class Date(datetime):
    def __new__(cls, *args):
        if len(args) == 1 and isinstance(args[0], str):
            return cls.strptime(args[0], "%d/%m/%Y")
        return datetime.__new__(cls, *args)
    def __str__(self):
        return self.strftime("%d/%m/%Y")
            
print("Esempio con classe derivata")    
n=Date('12/11/2010')
print(n, type(n))
print(n.year)

n=Date(2010, 12, 31)
print(n, type(n))
print(n.year)




