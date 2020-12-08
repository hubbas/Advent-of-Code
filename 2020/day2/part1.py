with open('input') as f:
	inputs = [i.strip().replace('-', ' ').replace(':', ' ').split() for i in f.readlines()]

def validate(low, high, char, password):
	c = password.count(char)
	return c >= int(low) and c <= int(high)

print(len(list(filter(lambda args: validate(*args), inputs))))
