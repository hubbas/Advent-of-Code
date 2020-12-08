with open('input') as f:
	inputs = [int(i.strip()) for i in f.readlines()]

def result():
	for i in inputs:
		for j in inputs:
			if (i + j) == 2020:
				return i * j

print(result())
