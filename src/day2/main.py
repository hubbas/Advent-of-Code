with open('input') as f:
	inputs = [i.strip().replace('-', ' ').replace(':', ' ').split() for i in f.readlines()]

# pw(0: low, 1: high, 2: char, 3: password)
def valid1(pw):
	c = pw[3].count(pw[2])
	return c >= int(pw[0]) and c <= int(pw[1])

def valid2(pw):
	l = pw[2] == pw[3][int(pw[0]) - 1]
	h = pw[2] == pw[3][int(pw[1]) - 1]
	return l != h

print('Part1:', len(list(filter(lambda x: valid1(x), inputs))))
print('Part2:', len(list(filter(lambda x: valid2(x), inputs))))
