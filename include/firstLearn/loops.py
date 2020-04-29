x = 0
while x < 10:
    print(x, end=' ')
    x += 1
print()
list1 = [1, 2, 3, 4]

while list1:
    print(list1.pop(), end=' ')

print()
list2 = ['lily', 'harry', 'eric']

print('直接元素迭代')
for name in list2:
    print(name, end=' ')

print()
print('从0开始，取len(list2)个元素')
for i in range(len(list2)):
    if list2[i] == 'harry':
        continue
    print(list2[i], end=' ')

print()
print('从0开始取10个元素')
for i in range(10):
    if i == 8:
        break
    print(i, end=' ')

print()
print('从1开始取3-1个元素')
for i in range(1, 3):
    print(i, end=' ')

print()
# if not isinstance(list2, int):
#     raise TypeError('参数错误 ！')
print()
for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)



