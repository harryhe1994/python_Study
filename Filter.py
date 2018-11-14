def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 3, 4])))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['a', '', 'B', None, 'C'])))

print(sorted([1, 5, 3, -1]))

print(sorted([1, 4, -2, -8], key=abs))

print(sorted(['bs', 'Zero', 'Token', 'Arron'], key=str.lower))
print(sorted(['bs', 'Zero', 'Token', 'Arron'], key=str.lower, reverse=True))
