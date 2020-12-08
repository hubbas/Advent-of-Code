with open('input') as f:
	inputs = [i.split('\n') for i in f.read().split('\n\n')]

"""
c = 0
for group in inputs:
	c += len(set(''.join(group)))
print(c)
"""
print(sum(map(len, map(set, map(lambda x: ''.join(x), inputs)))))
