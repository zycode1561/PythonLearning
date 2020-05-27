

"""

"""

__author__ = 'Zy_Code'

import functools

list1 = [1, 2, 3, 4, 5, 6]

# 降序排序
# list1.sort(reverse=True)
# 注意sorted是返回一个新的排序序列，下面我们就用sorted演示
# 直接.sort参数与sorted相似
print(sorted(list1, reverse=True))

# 根据元组中的某一个元素排序

list2 = [('a', 3), ('b', 2), ('c', 1)]
print(sorted(list2, key=lambda i: i[1]))  # 根据第二个元素排序

# 自定义函数排序，取模排序

list3 = [14, 7, 6, 9, 11, 24]
print(sorted(list3, key=functools.cmp_to_key(lambda x, y: x % 7 - y % 7)))

# 按照某两个元素进行排序，如果返回值中第一个元素相等，根据第二个元素排序

students = [("zhangsan", "A", 10), ("lisi", "C", 9), ("lisi1", "A", 9), ("lisi2", "B", 9), ("wangwu", "B", 13)]
print(sorted(students, key=lambda x: (x[2], x[1]), reverse=True))

# 对list部分排序
list4 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
list4[1:7] = sorted(list4[1:7], reverse=True)
print(list4)


