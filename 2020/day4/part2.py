with open('input') as f:
	inputs = [i.replace('\n', ' ') for i in f.read().split('\n\n')]
	inputs = [dict(s.split(':') for s in i.strip().split(' ')) for i in inputs]

valid_passports = list(filter(lambda passport:\
	all(key in passport for key in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')),
	inputs))

def validate_passport(passport):
	def validate_range(s, min, max):
		return int(s) >= min and int(s) <= max

	def validate_hgt(s):
		if s.endswith('cm'):
			return validate_range(s[:-2], 150, 193)
		elif s.endswith('in'):
			return validate_range(s[:-2], 59, 76)
		return False

	funcs = {
		'byr': lambda s: validate_range(s, 1920, 2002),
		'iyr': lambda s: validate_range(s, 2010, 2020),
		'eyr': lambda s: validate_range(s, 2020, 2030),
		'hgt': lambda s: validate_hgt(s),
		'hcl': lambda s: s[0] == '#' and len(s[1:]) == 6,
		'ecl': lambda s: s in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
		'pid': lambda s: len(s) == 9 and s.isdigit(),
		'cid': lambda s: True
	}

	return all(funcs[key](passport[key]) for key in passport)

print(len(list(filter(validate_passport, valid_passports))))
