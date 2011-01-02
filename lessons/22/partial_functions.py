import functools

def foo(a, b):
    print('a=', a)
    print('b=', b)

bar=functools.partial(foo, b=10)

bar(2)
