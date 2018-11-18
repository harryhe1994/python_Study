import os

print(os.name)
print(os.environ.get('PATH'))
print(os.path.abspath('.'))
print(os.path.join('D:\HarryHe\python_study\python_Study\FileOperation', 'testdir'))
# os.mkdir('D:/HarryHe/python_study/python_Study/FileOperation/testdir')
# os.rmdir('D:/HarryHe/python_study/python_Study/FileOperation/testdir')

print(os.listdir('.'))

for x in os.listdir('.'):
    if os.path.isfile(x):
        print(x)