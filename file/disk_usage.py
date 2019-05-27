from shutil import disk_usage

total, used, free = disk_usage('/')
print(total / 2**30, used / 2**30, free / 2**30)