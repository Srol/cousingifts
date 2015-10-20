import random

gifts = {}
Hogans = ["Erin", "Patrick", "Jane"]
Nyreens = ["Tom", "Kerry", "James", "Brendan"]
Vetters = ["Juliana", "Mary", "Laura", "Elizabeth"]
Jacobs = ["Galen", "Meghan"]
allcousins = ["Erin", "Patrick", "Jane", "Tom", "Kerry", "James", "Brendan","Juliana", "Mary", "Laura", "Elizabeth","Galen", "Meghan"]

for cousin in Hogans:
	match = random.choice(allcousins)
	while match in Hogans:
		match = random.choice(allcousins)
	gifts[cousin] = match
	allcousins.remove(match)
	
for cousin in Nyreens:
	match = random.choice(allcousins)
	while match in Nyreens:
		match = random.choice(allcousins)
	gifts[cousin] = match
	allcousins.remove(match)

for cousin in Vetters:
	match = random.choice(allcousins)
	while match in Vetters:
		match = random.choice(allcousins)
	gifts[cousin] = match
	allcousins.remove(match)

for cousin in Jacobs:
	match = random.choice(allcousins)
	while match in Jacobs:
		match = random.choice(allcousins)
	gifts[cousin] = match
	allcousins.remove(match)

listfile = open("listfile.txt", "w")

for key, value in gifts.iteritems():
	listfile.write(key + ": " + value + "\n")

listfile.close()