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

