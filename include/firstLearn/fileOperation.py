# w为覆盖写，a为追加写
with open('./test.txt', 'a') as f:
    f.write('\nThe time is 19:01')

with open('./test.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
