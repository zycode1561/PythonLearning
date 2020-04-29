zhang = 12345666
yun = zhang
print(id(zhang))
print(id(yun))
print(zhang is yun)
yun = 1234566
print(id(yun))
print(zhang is yun)

a = int(12345511111111)
b = 12345511111111
print(id(a))
print(id(b))

x = 99
if 20 < x < 50 or 100 > x > 80:
    print('if判断成功,ok')
elif x > 100:
    print('if判断错误,error')