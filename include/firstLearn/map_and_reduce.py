from functools import reduce


def f(x):
    return x * x


res1 = map(f, [1, 3, 4])
print(list(res1))


def f1(x, y):
    return x + y


res2 = reduce(f1, [1, 2, 4])
print(res2)


def not_empty(s: str):
    return s and s.strip()


# filter()函数返回的是一个Iterator，也就是一个惰性序列，
# 所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
res3 = list(filter(not_empty, ['A', '', ' ', 'CCC']))
print(res3)

# lambda作为一个表达式，定义了一个匿名函数，上例的代码x为入口参数，x+1为函数体
res4 = map(lambda x: x * 2, [1, 2, 3, 4])
print(list(res4))

res5 = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print(res5)
