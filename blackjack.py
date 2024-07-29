from itertools import product
import random

# build the deck

"""...
standard 52-deck of cards
4 suits: clubs♣, diamonds♦, hearts♥, spades♠
13 ranks in each of the 4 suits
each suit with three court cards; King, Queen, Jack. each worth 10 points
each suit also has 10 numerical(pip) cards: Ace(1) to 10
ace is worth 1 or 11

"""
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = ["King", "Queen", "Jack", "Ace"] +  list(range(2,11))

deck = {(suit, rank): 10 if rank in ["King", "Queen", "Jack"] else 11 if rank == 'Ace' else int(rank) for suit, rank in product(suits, ranks)}

# for card, value in deck.items():
# 	print(f"{card}, {value}")

# Adjust the value for Ace to be either 1 or 11
for (suit, rank) in deck:
	if rank == "Ace":
		deck[(suit, rank)] = [1, 11]

# gameplay
"""...
hit: take another card
stand: keep their current hand
players can be hit until they decide to stand or until hand value exceeds 21
hand needs to be checked everytime need option is check
stand:
"""
def calculate_hand_value(player_hand):
	# track the aces
	# loop the list
	# use the values to look up the values
	# sum the values found
	player_hand_value = 0
	num_aces = 0
	#iterable_player_hand = list(player_hand)
	for card in player_hand:
		# check if card in deck
		if card[1] == 'Ace':
			num_aces += 1
		else:
			player_hand_value += deck[card]

	# choose a value for aces 1 or 11 based on the current hand value
	for _ in range(num_aces):
		if player_hand_value + 11 <= 21:
			player_hand_value += 11
		else:
			player_hand_value += 1
	return player_hand_value

def hit(player_hand):
	# take another card -> randomly assign a valid card
	# randomly assign a card
	# use choice to randomly pick a key. Format: (suit, rank)
	# use the key to pick card's value. Format: 1-11
	random_card_key = random.choice(list(deck.keys()))
	#random_card_value = deck[random_card_key]
	#result_tuple = (random_card_key, random_card_value)
	player_hand.append(random_card_key)
	# print("Random selected card:", random_card)
	# print("Value of the card:", deck[random_card])


def stand(player_hand):
	# keep their current hand, do not modify hand
	return True




# winning or losing
