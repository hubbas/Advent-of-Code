with open('input') as f:
	inputs = [line.split() for line in f.readlines()]

acc, pc = 0, 0
visited = [0]
while True:
	ins, val = inputs[pc]
	if ins == 'jmp':
		pc += int(val) - 1
	elif ins == 'acc':
		acc += int(val)
	pc += 1	
	if pc in visited:
		break
	visited.append(pc)

print(acc)
