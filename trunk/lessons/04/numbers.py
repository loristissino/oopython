def FirstItem(a):
   if isinstance(a, tuple):
       return a[0]
   return a

#mynumbers=[ (12, 34), 13 ]

#mynumbers.sort()

mynumbers=[ (12, 34), 13 ]
mynumbers.sort(key=FirstItem)
print(mynumbers)

mynumbers=[ (12, 34), 11 ]
mynumbers.sort(key=FirstItem)
print(mynumbers)


