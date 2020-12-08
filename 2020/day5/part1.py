with open('input') as f:
	inputs = [line.strip() for line in f.readlines()]

ID = 0
for i in inputs:
	R = int(i[:7].replace('F', '0').replace('B', '1'), 2)
	C = int(i[7:].replace('L', '0').replace('R', '1'), 2)
	ID = max(R * 8 + C, ID)

print(ID)
