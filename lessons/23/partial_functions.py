import functools

def foo(a, b, c=0):
    print('a=', a)
    print('b=', b)
    print('c=', c)
    return 1

customfoo=functools.partial(foo, b=10, c=22)

'''
def customfoo(a):
    return foo(a, b=10, c=22)
'''

v=customfoo(2)
print(v)


