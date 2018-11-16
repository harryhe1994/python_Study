from io import BytesIO

f = BytesIO()
f.write('你好'.encode('utf-8'))
print(f.getvalue())
