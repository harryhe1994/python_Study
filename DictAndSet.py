names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
print(d['Michael'])
d['Harry'] = 85
print(d['Harry'])
# print(d['Harry1'])
print(d.get('Harry'))
print(d.get('Harry1'))
print('Harry' in d)
d.pop('Harry')
print(d)
print('Harry' in d)


s = set([1, 2, 2, 3, 3, 3])
print(s)
s.add(4)
print(s)
