from functools import reduce


def f(x):
    return x * x


r = map(f, [1, 2, 3])

print(list(r))


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7]))


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2num, '1235649')))

print(isinstance(reduce(fn, map(char2num, '1235649')), int))
