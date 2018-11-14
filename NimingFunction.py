print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

f = lambda x: x * x
print(f(5))


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('Hello')


now()
