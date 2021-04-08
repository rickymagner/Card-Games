""" Implementation of main Redjack game with player interaction."""

import sys
sys.path.append('..')

import deck
import points


class RedjackTable:
	""" A class to keep track of gameplay. """

	def __init__(self):
		self.deck = deck.Deck()
		self.deck.shuffle()
		self.player_hand = []
		self.dealer_hand = []
		for i in range(2):
			self.player_hand.append(self.deck.draw())
			self.dealer_hand.append(self.deck.draw())

		self.dealer_score = points.count_score(self.dealer_hand)
		self.player_score = points.count_score(self.player_hand)

	def status(self):
		print("Current situation:\n")
		print("Dealer's hand:\n")
		dealer_visible_hand = [self.dealer_hand[0], deck.Card(' ',' ')]
		deck.display_list(dealer_visible_hand)

		print("Player's hand:\n")
		deck.display_list(self.player_hand)	


	def print_dealer_score(self):
		print("Dealer score = " + str(self.dealer_score[0]) + " with red card " + str(self.dealer_score[1].value) + str(self.dealer_score[1].suit))

	def print_player_score(self):
		print("Player score = " + str(self.player_score[0]) + " with red card " + str(self.player_score[1].value) + str(self.player_score[1].suit))
		

	def hit(self):
		self.player_hand.append(self.deck.draw())
		self.player_score = points.count_score(self.player_hand)

	def dealer_draw(self):
		while (self.dealer_score[0] < 22) and (self.dealer_score[0] > -1) and (self.dealer_score[0] < self.player_score[0]):
			self.dealer_hand.append(self.deck.draw())
			self.dealer_score = points.count_score(self.dealer_hand)
		
def playGame():
	table = RedjackTable()
	print("Welcome to Redjack!\n")
	table.status()
	table.print_player_score()
	
	choice = 'n'
	choice = input("Would you like another hit? (y/n)")
	while (choice.lower() == 'y') and (table.player_score[0] < 22) and (table.player_score[0] > -1):
		table.hit()
		table.status()
		if (table.player_score[0] < 0) or (table.player_score[0] > 22):
			print("Player has gone over 21!")
			playAgain()
		table.print_player_score()
		choice = input("Would you like another hit? (y/n)")
	
	table.dealer_draw()
	print("---- Final Status ----")
	print("Dealer's Hand:")
	deck.display_list(table.dealer_hand)
	table.print_dealer_score()
	print("Player's Hand:")
	deck.display_list(table.player_hand)
	table.print_player_score()

	if (table.player_score[0] > table.dealer_score[0]) or (table.dealer_score[0] < 0) or (table.dealer_score[0] > 21):
		print("Player wins!!")
	elif table.player_score[0] == table.dealer_score[0]:
		print("Tie game!")
	elif table.player_score[0] < table.dealer_score[0]:
		print("Dealer wins!")
	playAgain()

def playAgain():
	again = input("Play again? (y/n)")
	if again.lower() == 'y':
		playGame()
	else:
		quit()

playGame()
