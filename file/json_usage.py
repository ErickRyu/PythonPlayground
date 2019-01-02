import json

f = open('train_condition.json', 'r')

val = json.load(f)

print(val)
