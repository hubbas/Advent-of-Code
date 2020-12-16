with open('input') as f:
	inputs = [int(line) for line in f.readlines()]

def contains_sum(nr, nrs):
	for i in range(len(nrs)):
		for j in range(i + 1, len(nrs)):
			if nr == nrs[i] + nrs[j]:
				return True
	return False

for i in range(25, len(inputs)):
	nr = inputs[i]
	nrs = inputs[i-25:i]
	if not contains_sum(nr, nrs):
		print(nr)
		break
