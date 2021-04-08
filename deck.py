""" We create a "card" class and a "deck" class to keep the
information used in a card game with some useful methods."""

import random


VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K', 'A']
SUITS = ['S', 'C', 'H', 'D']


class Card:
	""" A class abstracting the notion of a card."""

	def __init__(self, suit, value):
		self.suit = suit
		self.value = value
	
	# print card to screen
	def display(self):
		print('/------\\')
		print('|      |')
		print('|  ' + self.value + self.suit + '  |')
		print('|      |')
		print('\\------/')

def display_list(hand):
	size = len(hand)
	print('/------\\' * size)
	print('|      |' * size)
	for card in hand[:-1]:
		print('|  ' + card.value + card.suit + '  |', end="")
	print('|  ' + hand[-1].value + hand[-1].suit + '  |')
	print('|      |' * size)
	print('\\------/' * size)

class Deck:
	""" A class modeling the notion of a deck of cards."""

	def __init__(self):
		self.deck = []
		for val in VALUES:
			for suit in SUITS:
				self.deck.append(Card(suit, val))

	def shuffle(self):
		random.shuffle(self.deck)
	
	def draw(self):
		return self.deck.pop()

			
