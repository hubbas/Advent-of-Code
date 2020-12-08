with open('input') as f:
	inputs = [i.strip().replace('-', ' ').replace(':', ' ').split() for i in f.readlines()]

def validate(low, high, char, password):
	l = char == password[int(low) - 1]
	h = char == password[int(high) - 1]
	return l != h

print(len(list(filter(lambda args: validate(*args), inputs))))
