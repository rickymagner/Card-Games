# Card Games
##### Classic card games with a twist!

This module implements a simple "deck" of cards class in Python and then uses it to play some alternative versions of well-known card games. To play, simply clone this repository and follow the instructions under whichever game you'd like to try.

## Redjack

This plays similarly to "Blackjack," but with a catch: the player and dealer's scores are calculated where one card acts as the "red card," meaning it counts as negative points. Usual point assignments as in Blackjack still hold: face cards are always 10, and aces can be 1 or 11 depending on which is better. Each turn, the player can either "hit" and get another card, or hold and let the dealer draw. The goal is to get as close to 21 points as possible without going over. If both the player and dealer get equal points or go over, then it's a tie.

Ex. Given a hand of: 4H, AC, KD, 5D (4 of hearts, ace of clubs, king of diamonds, 5 of diamonds), your score is either:
* -4 + 11 + 10 + 5 = 22 (4H as "red card"; ace as 11; over!) OR -4 + 1 + 10 + 5 = 12 (4H as "red card"; ace as 1)
* 4 - 1 + 10 + 5 = 18 (AC as "red card"; ace as 1) OR 4 - 11 + 10 + 5 = 8 (AC as "red card"; ace as 11)
* Etc.

This implementation automatically calculates the optimal red card and presents the score to the player. 

### How to Play

Once you have the repository available locally, navigate to the Redjack directory and run `python game.py`. Each turn you decide whether you want to "hit" and draw a new card (y/n). The output will update with the situation, drawing cards with the suit and value printed on them. 

![Example of gameplay](Redjack/gameplay.jpg)
