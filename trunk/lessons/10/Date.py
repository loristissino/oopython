"""
import datetime
"""
"""
class MyDate(datetime.date):
   def __new__(cls, value):
       datetime.date.__new__(cls, datetime.date.fromtimestamp(1)) # strptime(value, "%d/%m/%Y"))
"""

"""       

class MyDate(datetime):
   def __new__(self, value):
       self = datetime.strptime(value, "%d/%m/%Y")
"""

from datetime import *

class MyDate():
    def __init__(self, value):
        self.__date=datetime.strptime(value, "%d/%m/%Y")
    def getYear(self):
        return self.__date.year
    def getMonth(self):
        return self.__date.month
    def getDay(self):
        return self.__date.day

    
n=MyDate('20/10/2010')
print(n, type(n))
print(n.getYear())



class MyDate(datetime):
    def __new__(cls, *args):
        if len(args) == 1 and isinstance(args[0], str):
            print("prima chiamata ** ", end='')
            print(args[0])
            return super().strptime(args[0], "%d/%m/%Y")
        print("seconda chiamata ** ", end='')
        print(*args)
        return datetime.__new__(cls, *args)

a=MyDate('12/11/2010')


