with open('input') as f:
	inputs = [i.split('\n') for i in f.read().strip().split('\n\n')]

"""
c = 0
for group in inputs:
	sets = [set(person) for person in group]
	inter = sets[0].intersection(*sets)
	c += len(inter)
print(c)
"""
m = map(lambda group: [set(person) for person in group], inputs)
m = map(lambda group: group[0].intersection(*group), m)
m = map(len, m)
print(sum(m))
