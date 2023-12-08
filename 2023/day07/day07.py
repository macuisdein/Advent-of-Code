import operator
file = open("input.txt", "r")
hands_rank = file.readlines()

number_hands = len(hands_rank) + 1



card_ranks_value = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}
card_ranks = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
five_kinds=[]
four_kinds=[]
full_houses = []
three_kinds = []
two_pairs = []
pairs = []
high_cards = []

for number in range(1, number_hands):
	cards = hands_rank[number - 1].split()[0] 
	bid = hands_rank[number - 1].split()[1]
	hand_max = ''
	hand_count = {"2":0, "3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"T":0,"J":0,"Q":0,"K":0, "A":0}
	for rank in card_ranks:
		for card in cards:
			if rank == card:
				hand_count[card] = hand_count[card] + 1
	#print(f"Hand count {hand_count}")
	if 5 in hand_count.values():
		five_kinds.append((cards,bid))
	elif 4 in hand_count.values():
		four_kinds.append((cards,bid))
	elif 3 in hand_count.values():
		if 2 in hand_count.values():
			full_houses.append((cards,bid))
		else:
			three_kinds.append((cards,bid))
	else:
		hand_values = list(hand_count.values())
		if hand_values.count(2) == 2:
			two_pairs.append((cards,bid))
		elif hand_values.count(2) == 1:
			pairs.append((cards,bid))
		else:
			high_cards.append((cards,bid))

# print(f"Five kinds: {five_kinds}")
# print(f"Four kinds: {four_kinds}")
# print(f"Full houses: {full_houses}")
# print(f"Three kinds: {three_kinds}")
# print(f"Two pairs: {two_pairs}")
# print(f"Pairs: {pairs}")
# print(f"High cards: {high_cards}")

my_order='23456789TJQKA'


if five_kinds:
	five_kinds = list(sorted(five_kinds, key=lambda word: [my_order.index(c) for c in word[0]]))
if four_kinds:
	four_kinds = list(sorted(four_kinds, key=lambda word: [my_order.index(c) for c in word[0]]))
if full_houses:
	full_houses = list(sorted(full_houses, key=lambda word: [my_order.index(c) for c in word[0]]))
if three_kinds:
	three_kinds = list(sorted(three_kinds, key=lambda word: [my_order.index(c) for c in word[0]]))
if two_pairs:
	two_pairs = list(sorted(two_pairs, key=lambda word: [my_order.index(c) for c in word[0]]))
if pairs:
	pairs = list(sorted(pairs, key=lambda word: [my_order.index(c) for c in word[0]]))
if high_cards:
	high_cards = list(sorted(high_cards, key=lambda word: [my_order.index(c) for c in word[0]]))

# print(f"Five kinds: {five_kinds}")
# print(f"Four kinds: {four_kinds}")
# print(f"Full houses: {full_houses}")
# print(f"Three kinds: {three_kinds}")
# print(f"Two pairs: {two_pairs}")
# print(f"Pairs: {pairs}")
# print(f"High cards: {high_cards}")

total_score = 0

hands_in_rank_order = high_cards + pairs + two_pairs + three_kinds + full_houses + four_kinds + five_kinds

for x in range(0, number):
	# print(f"Score: {hands_in_rank_order[x][1]} and rank {x + 1}")
	total_score = total_score + (int(hands_in_rank_order[x][1]) * (x+1))

print(f"Part 1 score: {total_score}")	

# Part 2

five_kinds=[]
four_kinds=[]
full_houses = []
three_kinds = []
two_pairs = []
pairs = []
high_cards = []

for number in range(1, number_hands):
	cards = hands_rank[number - 1].split()[0] 
	bid = hands_rank[number - 1].split()[1]
	hand_max = ''
	hand_count = {"2":0, "3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"T":0,"J":0,"Q":0,"K":0, "A":0}
	for rank in card_ranks:
		for card in cards:
			if rank == card:
				hand_count[card] = hand_count[card] + 1
	# print(f"Hand count {hand_count}")
	
	if (hand_count["J"] > 0) and (hand_count["J"]!=5):
		# print(f"Before joker, hand count: {hand_count}")
		joker_count = hand_count["J"]
		# print(f"Joker count: {joker_count}")
		hand_count["J"] = 0
		highest_card = max(hand_count.items(), key=operator.itemgetter(1))[0]
		# print(f"Highest card = {highest_card}")
		hand_count[highest_card] = hand_count[highest_card] + joker_count
		# print(f"After joker, hand count: {hand_count}")	 	
	if 5 in hand_count.values():
		five_kinds.append((cards,bid))
	elif 4 in hand_count.values():
		four_kinds.append((cards,bid))
	elif 3 in hand_count.values():
		if 2 in hand_count.values():
			full_houses.append((cards,bid))
		else:
			three_kinds.append((cards,bid))
	else:
		hand_values = list(hand_count.values())
		if hand_values.count(2) == 2:
			two_pairs.append((cards,bid))
		elif hand_values.count(2) == 1:
			pairs.append((cards,bid))
		else:
			high_cards.append((cards,bid))

my_order='J23456789TQKA'


if five_kinds:
	five_kinds = list(sorted(five_kinds, key=lambda word: [my_order.index(c) for c in word[0]]))
if four_kinds:
	four_kinds = list(sorted(four_kinds, key=lambda word: [my_order.index(c) for c in word[0]]))
if full_houses:
	full_houses = list(sorted(full_houses, key=lambda word: [my_order.index(c) for c in word[0]]))
if three_kinds:
	three_kinds = list(sorted(three_kinds, key=lambda word: [my_order.index(c) for c in word[0]]))
if two_pairs:
	two_pairs = list(sorted(two_pairs, key=lambda word: [my_order.index(c) for c in word[0]]))
if pairs:
	pairs = list(sorted(pairs, key=lambda word: [my_order.index(c) for c in word[0]]))
if high_cards:
	high_cards = list(sorted(high_cards, key=lambda word: [my_order.index(c) for c in word[0]]))


total_score = 0

hands_in_rank_order = high_cards + pairs + two_pairs + three_kinds + full_houses + four_kinds + five_kinds

for x in range(0, number):
	# print(f"Score: {hands_in_rank_order[x][1]} and rank {x + 1}")
	total_score = total_score + (int(hands_in_rank_order[x][1]) * (x+1))

print(f"Part 2 score: {total_score}")	
