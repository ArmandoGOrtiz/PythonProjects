# Armando Ortiz
# Project 5
# 6-6-19

#card class
class Card:
    #card class has rank and suit
    def __init__(self, the_rank, the_suit ):
        self.rank = the_rank
        self.suit = the_suit
    # suit color of black or red    
    def color(self):
        if self.suit == "C":
            return "black"
        if self.suit == "S":
            return "black"
        if self.suit == "D":
            return "red"
        if self.suit == "H":
            return "red"
    # what symbols of deck
    def __str__(self):
        symbols = ["", "", "2", "3", "4", "5", "6", "7", 
        "8", "9", "10", "J", "Q", "K", "A"]
        return symbols[self.rank] + self.suit
    
    def __repr__(self):
        return str(self)
    #allows for card sort
    def __lt__(self,other):
        if self.rank < other.rank:
            return True
    
    def __eq__(self, other):
        if self.rank == other.rank:
            return True
