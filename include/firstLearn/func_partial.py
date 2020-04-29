import functools

int2 = functools.partial(int, base=2)

num1 = int2('10011001')
print(num1)
print(type(num1))

s = bin(num1)
s_oct = oct(num1)
s_hex = hex(num1)
print(s)
# print(s[2:])
print(s_oct)
print(s_hex)

for i in range(8):
    print(num1 | 1 << i, end=' ')

print()

for i in range(8):
    print(num1 & 1 << i, end=' ')