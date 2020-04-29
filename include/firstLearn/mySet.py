list1 = [1, 2, 3, 4, 1, 2, 10]

list1 = set(list1)

print(list1)

set1 = {1, 2, 3, 4, 4, 5, 5, 6}
print(set1)

print(list1.union(set1))

print(list1 & set1)
print(list1 | set1)
print(list1 - set1)
print(set1 - list1)

set1.add(7)
print(set1)
set1.update([10, 11, 12])
set1.remove(3)
set1.pop()
print(set1)