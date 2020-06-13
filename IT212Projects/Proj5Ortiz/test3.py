# Armando Ortiz
# Project 5
# 6-6-19

from cardb import Card
from deckb import Deck
from pokerhand import PokerHand
from constants import *

# initalize counts array 
counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for loops that create deck object able to use all methods poker hand array created
for i in range(0,2000):
    deck = Deck()
    deck.shuffle()
    poker_hands = [ ]
    # creates arr array and deals deck to pokerhand object 
    for i in range(0,5):
        arr = []
        for i in range(0,5):
            arr.append(deck.deal())
        ph = PokerHand(arr)
        poker_hands.append(ph)
        # classifies poker hands
    for ph in poker_hands: 
        ph.classify()
        # counts the hands on pokerhand object   
    for ph in poker_hands:
     counts[ph.hand_type] += 1
# prints all the occurances 
print("Number of Occurrences of each Hand Type")
print("=======================================")
print(f"Straight Flush: {counts[STRAIGHT_FLUSH]}")
print(f"Four of a Kind: {counts[FOUR_OF_A_KIND]}")
print(f"FULL_HOUSE: {counts[FULL_HOUSE]}")
print(f"FLUSH: {counts[FLUSH]}")
print(f"STRAIGHT: {counts[STRAIGHT]}")
print(f"THREE_OF_A_KIND: {counts[THREE_OF_A_KIND]}")
print(f"TWO_PAIR: {counts[TWO_PAIR]}")
print(f"ONE_PAIR: {counts[ONE_PAIR]}")
print(f"NO_PAIR: {counts[NO_PAIR]}")