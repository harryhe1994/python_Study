from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('World')
f.write('中文')
print(f.getvalue())