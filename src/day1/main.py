with open('input') as f:
	inputs = [int(i.strip()) for i in f.readlines()]

def part1():
	for i in inputs:
		for j in inputs:
			if (i + j) == 2020:
				return i * j

def part2():
	for i in inputs:
		for j in inputs:
			for k in inputs:
				if (i + j + k) == 2020:
					return i * j * k

print('Part1:', part1())
print('Part2:', part2())
