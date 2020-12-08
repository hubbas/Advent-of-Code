with open('input') as f:
	inputs = [l.strip() for l in f.readlines()]

def slope(right, down):
	cr, hits = 0, 0
	for i in range(down, len(inputs), down):
		f = inputs[i]
		cr += right
		if f[cr % len(f)] == '#':
			hits += 1
	return hits

print(slope(3, 1))
