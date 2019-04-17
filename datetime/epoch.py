import os
import time


def print_time():
    print(time.strftime("%Y-%m-%d %H:%M:%S +0000", time.localtime(1554975584)))


print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(1554975584)))

os.environ['TZ'] = 'US/Eastern'
print_time()
#print(time.strftime("%Y-%m-%d %H:%M:%S +0000", time.localtime(1554975584)))

os.environ['TZ'] = 'Europe/Brussels'
print_time()
#print(time.strftime("%Y-%m-%d %H:%M:%S +0000", time.localtime(1554975584)))


