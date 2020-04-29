import calendar
import time

print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print(calendar.month(2020, 4))


