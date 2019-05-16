
def ignore_msb(value_to_change):
    return value_to_change & 127


for i in range(0, 256):
    print(i, ignore_msb(i))