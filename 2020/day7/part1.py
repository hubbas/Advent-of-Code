import re

with open('input') as f:
	inputs = [re.split(',|bag[s]*|contain|no other|\.|\d+|\n', line) for line in f.readlines()]

def count_bags(bag_to_find):
	all_bags = {}
	for i in inputs:
		bag = [b.strip() for b in i if b.strip()]
		all_bags[bag[0]] = bag[1:]

	def find_bag_rec(bags, found):
		if bag_to_find in bags:
			found = True
		for bag in bags:
			found = find_bag_rec(all_bags[bag], found)
		return found
	
	return sum([find_bag_rec(bags, False) for bags in all_bags.values()])

print(count_bags('shiny gold'))
