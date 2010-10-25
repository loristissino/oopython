"""
See http://tinyurl.com/oopython
"""

from datetime import *

class Date(datetime):
    def __new__(cls, *args):
        if len(args) == 1 and isinstance(args[0], str):
            return cls.strptime(args[0], "%d/%m/%Y")
        return datetime.__new__(cls, *args)
    def __str__(self):
        return self.strftime("%d/%m/%Y")
            
