import re

hand = open('OpenSkills.json')
for line in hand:
    line = line.rstrip()
    #if line.find('LifePoint') >= 0:
    #    print(line)
    if re.search('^.*\sCPR', line):
        print(line)

x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('\S+?@\S+', x)
print(y)
