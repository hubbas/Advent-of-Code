with open('input') as f:
	inputs = [i.replace('\n', ' ') for i in f.read().split('\n\n')]
	inputs = [dict(s.split(':') for s in i.strip().split(' ')) for i in inputs]

valid_passports = list(filter(lambda passport:\
	all(key in passport for key in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')),
	inputs))

print(len(valid_passports))
