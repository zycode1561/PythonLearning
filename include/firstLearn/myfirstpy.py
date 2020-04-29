name = "hello" + " " + "world"
print(name * 3)

print(len(name))

words = name.split(" ")
print(words)
print(type(words))

name_str = '-'
res = name_str.join(words)
print(res)

name = name.replace('l', '1')

print(name.upper())
print(name.lower())

places = "   aaa  s ds  "
print(places.strip())
print(places.lstrip())
print(places.rstrip())

String = '{},{},{}\n'.format('ni', 'hao', 'a')
print(String)

String1 = '{2},{1},{0}\n'.format('ni', 'hao', 'a')
print(String1)

String2 = '{x},{y},{z}'.format(x=1, y=2, z=3)
print(String2)


