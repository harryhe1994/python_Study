import pickle

d = dict(name='Harry', age=24, score=88)
print(pickle.dumps(d))

with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)

with open('dump.txt', 'rb') as f:
    d = pickle.load(f)
    print(d)
