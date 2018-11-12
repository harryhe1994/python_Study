classmates = ['Mike', 'Tom', 'Jack']
length = len(classmates)
print(length)
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])
print(classmates[-3] == classmates[0])
classmates.append('Kelvin')
print(classmates)
classmates.insert(1, 'Harry')
print(classmates)
# classmates.pop()
# print(classmates)
classmates.pop(-2)
print(classmates)

t = (1,)
print(t)
t = ('a', 'b', ['A', 'B'])
print(t)
print(t[2][0])
print(t[2][1])

age = 20
if age >= 18:
    print('your age is:', age)
    print('adult')

age = 3
if age >= 18:
    print('your age is:', age)
    print('adult')
else:
    print('your age is:', age)
    print('teenager')
print('hhkjjj\n')

print('---------------\n')
for name in classmates:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum += x
print(sum)

print('------------\n')
sum = 0
for x in range(101):
    sum += x
print(sum)