# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

a = 10


def add_ab(b, c) -> (int, int):
    return b + c, 0


res = add_ab(1, 2)
res1, res2 = add_ab(3, 4)
print(res1, res2)
print(res[1])


def add_ab(x=1, b=2, c=3):
    return x + b + c


# res = add_ab(3, 4, 5)
res = add_ab()
print(res)


def add_list(n, *args):
    for i in args:
        n += i
    return n


res = add_list(1, 2, 3)

print(res)


def add_nums(num, **kwargs):
    for arg, value in kwargs.items():
        print(arg, value)


add_nums(1, x=1, y=2)


# 会返回一个生成器
def fib(n):
    x, y, z = 0, 0, 1
    while x < n:
        yield z
        y, z = z, y + z
        x = x + 1
    return 'done'


i = fib(6)
print(next(i))
print(next(i))
print(next(i))

for a in fib(6):
    print(a, end=' ')
print()


# 杨辉三角
def triangles():
    L = [1]
    yield L
    while 1:
        a = [*L]
        a.append(0)
        b = [*L]
        b.insert(0, 0)
        L = [a[i] + b[i] for i in range(0, len(a))]
        yield L


item = triangles()

print(next(item))
print(next(item))
print(next(item))
print(next(item))
