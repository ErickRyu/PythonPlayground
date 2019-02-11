import os

target_directory = './level_A/level_B/level_C'

if not os.path.exists(target_directory):
            os.makedirs(target_directory)
            os.chmod(target_directory, 0o777)

print(target_directory)

print(target_directory.split('/')[-1])