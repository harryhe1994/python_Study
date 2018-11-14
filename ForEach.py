d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

a = [x * x for x in range(1, 11)]
print(a)

print([m + n for m in 'ABC' for n in 'XYZ'])

print([x * x for x in range(1, 11) if x % 2 == 0])

import os

print([d for d in os.listdir('.')])


g = (x * x for x in range(1, 11))
print(g)
print(next(g))
print('-------')


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1


f = fab(5)
# print(next(f))
print(f.__next__())
print(f.__next__())
print(next(f))
print(next(f))
print(next(f))

from inspect import isgeneratorfunction
print(isgeneratorfunction(fab))


it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
        print('x = ', x)
    except StopIteration:
        break
