""" Methods for computing the value of a hand using Redjack rules."""

POINTS = {
	'2': 2,
	'3': 3,
	'4': 4,
	'5': 5,
	'6': 6,
	'7': 7,
	'8': 8,
	'9': 9,
	'X': 10,
	'J': 10,
	'Q': 10,
	'K': 10
}

def old_count_score(hand):
	# start by counting aces in hand
	num_aces = 0
	tmp_hand = hand
	ace = 0
	for card in tmp_hand:
		if card.value == 'A':
			num_aces += 1
			tmp_hand.remove(card)
			ace = card
	
	# calculate possible scores given hand
	totals = []
	non_ace_total = sum([POINTS[x.value] for x in tmp_hand])
	for i in range(num_aces+1):
		totals.append(non_ace_total + 1*i + 11*(num_aces - i))
	
	# cycle through possible "redjack" cards
	redjack_scores = []
	for t in totals:
		for card in tmp_hand:
			redjack_scores.append((t - 2*POINTS[card.value], card))
		if num_aces > 0:
			redjack_scores.append((t - 2, ace))
			redjack_scores.append((t - 11, ace))
	
	score_list = [x[0] for x in redjack_scores]
	max_score = max([x for x in score_list if x < 22])
	red_card = next(x[1] for x in redjack_scores if x[0] == max_score)

	return (max_score, red_card)

def count_score(hand):
	# start by counting aces in hand
	num_aces = 0
	tmp_hand = hand[:]
	ace = 0
	for card in tmp_hand:
		if card.value == 'A':
			num_aces += 1
			ace = card
			tmp_hand.remove(card)
	
	# explore possible red cards
	non_ace_total = sum([POINTS[card.value] for card in tmp_hand])
	non_ace_redjack_scores = []
	for card in tmp_hand:
		non_ace_redjack_scores.append((non_ace_total - 2*POINTS[card.value], card))
	
	non_ace_max_score = -1
	non_ace_red_card = hand[0]
	for pair in non_ace_redjack_scores:
		if (pair[0] > non_ace_max_score) and (pair[0] < 22):
			non_ace_max_score = pair[0]
			non_ace_red_card = pair[1]

	if num_aces == 0:
		return (non_ace_max_score, non_ace_red_card)

	elif num_aces > 0:
		# first ace acts as 1
		ace_redjack_scores_1 = [(x[0]+1, x[1]) for x in non_ace_redjack_scores]
		ace_max_score_1 = -1
		ace_red_card_1 = hand[0]
		for pair in ace_redjack_scores_1:
			if (pair[0] > ace_max_score_1) and (pair[0] < 22):
				ace_max_score_1 = pair[0]
				ace_red_card_1 = pair[1]

		# then ace acts as 11
		ace_redjack_scores_E = [(x[0]+11, x[1]) for x in non_ace_redjack_scores]
		ace_max_score_E = -1
		ace_red_card_E = hand[0]
		for pair in ace_redjack_scores_E:
			if (pair[0] > ace_max_score_E) and (pair[0] < 22):
				ace_max_score_E = pair[0]
				ace_red_card_E = pair[1]

		# ace as red card, noting A = 11 never optimal
		ace_redjack_scores_R = [(x[0]-1, x[1]) for x in non_ace_redjack_scores]
		ace_max_score_R = -1
		for pair in ace_redjack_scores_R:
			if (pair[0] > ace_max_score_R) and (pair[0] < 22):
				ace_max_score_R = pair[0]
		

		if num_aces == 1:
			# compare possibilities
			results = [(ace_max_score_1, ace_red_card_1), (ace_max_score_E, ace_red_card_E), (ace_max_score_R, ace)]
			scores = [x[0] for x in results]
			ind = scores.index(max(scores))
			return results[ind]

		if num_aces == 2:
			# first & second aces act as 1
			ace_redjack_scores_11 = [(x[0]+2, x[1]) for x in non_ace_redjack_scores]
			ace_max_score_11 = -1
			ace_red_card_11 = hand[0]
			for pair in ace_redjack_scores_11:
				if (pair[0] > ace_max_score_11) and (pair[0] < 22):
					ace_max_score_11 = pair[0]
					ace_red_card_11 = pair[1]

			# first as 1 & second as 11
			ace_redjack_scores_1E = [(x[0]+1, x[1]) for x in non_ace_redjack_scores]
			ace_max_score_1E = -1
			ace_red_card_1E = hand[0]
			for pair in ace_redjack_scores_1E:
				if (pair[0] > ace_max_score_1E) and (pair[0] < 22):
					ace_max_score_1E = pair[0]
					ace_red_card_1E = pair[1]

			# ace as red card, forcing net ace difference to 0 or 10
			ace_redjack_scores_R2 = [(x[0]+10, x[1]) for x in non_ace_redjack_scores]
			ace_max_score_R2 = -1
			for pair in ace_redjack_scores_R2:
				if (pair[0] > ace_max_score_R2) and (pair[0] < 22):
					ace_max_score_R2 = pair[0]

			# compare possibilities
			results = [(ace_max_score_11, ace_red_card_11), (ace_max_score_1E, ace_red_card_1E), (ace_max_score_R2, ace)]
			scores = [x[0] for x in results]
			ind = scores.index(max(scores))
			return results[ind]

		if num_aces == 3:
			if len(hand) == 3:
				return (21, ace)

		return (63, hand[0])

