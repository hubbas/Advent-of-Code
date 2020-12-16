with open('input') as f:
	inputs = [int(line) for line in f.readlines()]

def contains_sum(nr, nrs):
	for i in range(len(nrs)):
		for j in range(i + 1, len(nrs)):
			if nr == nrs[i] + nrs[j]:
				return True
	return False

def find_sum(nr_to_find, nrs_sublist):
	queue = []
	for nr in nrs_sublist:
		queue.append(nr)
		s = sum(queue)
		while s > nr_to_find:
			queue.pop(0)
			s = sum(queue)
		if s == nr_to_find:
			queue = sorted(queue)
			return queue[0] + queue[-1]

for i in range(25, len(inputs)):
	nr = inputs[i]
	nrs = inputs[i-25:i]
	if not contains_sum(nr, nrs):
		print(find_sum(nr, inputs[:i]))
		break
