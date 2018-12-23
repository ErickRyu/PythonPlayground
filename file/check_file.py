import os

flag_exist = os.path.exists('sample_file.txt')
print(flag_exist)

file_size = os.path.getsize('sample_file.txt')
print(file_size)
