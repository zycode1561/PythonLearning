def get_pers(arr, x, cur, used):
    if x == len(cur):
        s = str()
        for i in cur:
            s += str(i)
        print(s, end=' ')
    for i in range(len(arr)):
        if used[i] or (len(cur) == 0 and arr[i] == 0):
            continue
        cur.append(arr[i])
        used[i] = True
        get_pers(arr, x, cur, used)
        cur.pop()
        used[i] = False


array1 = [1, 0, 0, 4]
array2 = [1, 0, 2, 3]
n = 3
used = [False] * len(array2)
curr = []
get_pers(array1, n, curr, used)
print()
get_pers(array2, n, curr, used)
