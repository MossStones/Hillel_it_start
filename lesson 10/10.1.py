def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    last = begin
    yield last
    for _ in range(end):
        last = func(last)
        yield last
from inspect import isgenerator

gen = some_gen(2, 3, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
