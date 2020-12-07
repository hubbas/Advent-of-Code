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

print('Part1:', slope(3, 1))
print('Part2:', slope(1, 1) * slope(3, 1) * slope(5, 1) * slope(7, 1) * slope(1, 2))
