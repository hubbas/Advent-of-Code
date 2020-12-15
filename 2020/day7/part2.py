import re

with open('input') as f:
	inputs = [re.split(',|bag[s]*|contain|no other|\.|\n', line) for line in f.readlines()]

def count_bags(bag_to_find):
	all_bags = {}
	for i in inputs:
		bag = [b.strip() for b in i if b.strip()]
		all_bags[bag[0]] = bag[1:]

	def find_bag_rec(bags):
		r = 1
		for bag in bags:
			r += (int(bag[0]) * find_bag_rec(all_bags[bag[2:]]))
		return r
	
	return find_bag_rec(all_bags[bag_to_find]) - 1

print(count_bags('shiny gold'))
