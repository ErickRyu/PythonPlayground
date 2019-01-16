
pair_dict = dict()

pair_dict = {'b':100, 'c':50, 'a':2}

print(pair_dict)

print(min(pair_dict))
print(max(pair_dict))
sorted_list = sorted(pair_dict.items(), key=lambda x: x[1])
print(sorted_list[1][1])
