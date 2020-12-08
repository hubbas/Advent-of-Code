with open('input') as f:
	inputs = [line.strip() for line in f.readlines()]

IDs = []
for i in inputs:
	R = int(i[:7].replace('F', '0').replace('B', '1'), 2)
	C = int(i[7:].replace('L', '0').replace('R', '1'), 2)
	IDs.append(R * 8 + C)

IDs = sorted(IDs)
for i in range(IDs[0], IDs[-1]):
	i1 = i - 1
	i2 = i + 1
	if i not in IDs and i1 in IDs and i2 in IDs:
		print(i)
		break
