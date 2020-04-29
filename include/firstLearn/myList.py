zhang = []
print(type(zhang))

zhang.append(1)
print(zhang)

zhang = ['1', 2, 3.5]
print(zhang)

zhang.append([4, 5, 6])
print(zhang)

len(zhang)

a = ['12', '23']
b = ['a', 'ab', 'abc']
print(a + b)
a = a * 3
print(a * 3)

print(a[2:3])

b[1] = 'b'
print(b)

b[1:3] = ['b', 'c']
print(b)

del b[0]
print(b)

print(a)
print(a.count('12'))
del a[2:]
print(a)

print('12' in a)

name = 'zhang yun'
print('zhang' in name)

fruits = ['apple', 'banana', 'apple']
print(fruits.index('apple', 1))

other = [1, 2, 3]
fruits += other
print(fruits)

fruits.insert(3, '0')
print(fruits)

fruits.remove('apple')
print(fruits)

print(fruits.pop(3))
print(fruits.pop())
print(fruits)

nums = [1, 124, 25, 36, 123]
nums.sort()
print(nums)

nums1 = sorted(nums)
print(nums1)

nums1.reverse()
print(nums1)

sli = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sli[-3:])
print(sli[:6:2])
print(sli[::3])

s = 'hello world'
print(s[6:])

list2 = list(range(12))
print(list2)

# 列表生成式
list3 = [x * x for x in range(1, 11)]
print(list3)

# if加后面是过滤条件
list4 = [x * x for x in range(1, 11) if x % 2 == 0]
print(list4)

list5 = [m + n for m in 'ABC' for n in 'DEF']
print(list5)

list6 = [x * 2 if x % 2 == 0 else -x for x in range(1, 10)]
print(list6)

# 把中括号换成小括号会编程一个生成器
list7 = (x * 2 if x % 2 == 0 else -x for x in range(1, 10))
print(next(list7))
print(next(list7))
for item in list7:
    print(item, end=' ')

print()
list8 = sorted([36, 5, -12, 9, -21], key=abs)
print(list8)

list9 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(list9)