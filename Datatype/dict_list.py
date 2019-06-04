import copy

pair_dict = dict()

pair_dict = {'b': 100, 'c': 50, 'a': 2}

print('test print', pair_dict)

if 'b' in pair_dict:
    print('b is ', pair_dict['b'])
    pair_dict.pop('b')

print(pair_dict)

print(min(pair_dict))
print(max(pair_dict))
sorted_list = sorted(pair_dict.items(), key=lambda x: x[1])
print(sorted_list)

copied_dict = copy.deepcopy(pair_dict)
copied_dict.pop('c')
copied_dict['g'] = 12
print(copied_dict)

print('show:', pair_dict.get('d', 'null'))

test_list = list()

test_list.append('1')

print(test_list)


test = {}
test['open'] = ''

print(test)

test['open'] = {'calc_time': 1234}

print(test)