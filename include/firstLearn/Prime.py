def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0  # lambda表达式相当于遍历it序列取到x，执行后面的判断并返回


def primes():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)  # 构建新序列


res = primes()
print(next(res))
print(next(res))
print(next(res))
print(next(res))