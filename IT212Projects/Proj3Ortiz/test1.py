# Armando Ortiz
# Project 3a
# 5-2-19

#from card.py import card class
from deck import Deck
from card import Card

#test the __init__ and __str__ methods
d = Deck( )
print(d, "\n")
#test the deal method
c=d.deal()
print (c)
#test the add_to_top method
d = Deck( )
c = Card(12, "S")
d.add_to_top(c)
print(d)
#test the add_to_bottom method
d = Deck( )
c = Card(12, "S")
d.add_to_bottom(c)
print(d)
#test the count method
c = d.count()
print(d)
#test the is_empty method
c = d.is_empty
print(c)
#test the shuffle method
d = Deck()
c = Card(12, "S")
d.shuffle()
print(d)

c = Card(12, "S")
e = Card(13, "D")
f = e.rank - c.rank