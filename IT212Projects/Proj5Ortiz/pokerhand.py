# Armando Ortiz
# Project 5
# 6-6-19

from cardb import Card
from deckb import Deck
from constants import *

class PokerHand:
    # creates array and put array in it
    def __init__(self,the_array):
        self._cards = []
        self._cards.extend(the_array)
        hand_type = UNCLASSIFIED
    #classifies poker hand with all cases for NO_PAIR,ONE_PAIR,TWO_PAIR, THREE_OF_A_KIND, STRAIGHT, FLUSH,FULL_HOUSE, FOUR_OF_A_KIND, STRAIGHT_FLUSH  
    def classify(self):
        self._cards.sort( )

        if self._cards[0].suit == self._cards[1].suit and \
         self._cards[1].suit == self._cards[2].suit and \
         self._cards[2].suit == self._cards[3].suit and \
         self._cards[3].suit == self._cards[4].suit and \
         self._cards[0].rank == self._cards[1].rank -1 and \
         self._cards[1].rank == self._cards[2].rank-1 and \
         self._cards[2].rank == self._cards[3].rank-1 and \
         self._cards[3].rank == self._cards[4].rank-1:

          self.hand_type = STRAIGHT_FLUSH

        elif  self._cards[0] == self._cards[1] and \
          self._cards[1] == self._cards[2] and \
          self._cards[2] == self._cards[3]:

          self.hand_type = FOUR_OF_A_KIND

        elif self._cards[1] == self._cards[2] and \
         self._cards[2] == self._cards[3] and \
         self._cards[3] == self._cards[4]:

          self.hand_type = FOUR_OF_A_KIND
        
        elif self._cards[0] == self._cards[1] and \
         self._cards[1] == self._cards[2] and \
         self._cards[3] == self._cards[4]:

          self.hand_type = FULL_HOUSE
        
        elif self._cards[0] == self._cards[1] and \
         self._cards[2] == self._cards[3] and \
         self._cards[3] == self._cards[4]:

          self.hand_type = FULL_HOUSE

        elif self._cards[0].suit == self._cards[1].suit and \
         self._cards[1].suit == self._cards[2].suit and \
         self._cards[2].suit == self._cards[3].suit and \
         self._cards[3].suit == self._cards[4].suit:

          self.hand_type = FLUSH
       
        elif self._cards[0].rank == self._cards[1].rank -1 and \
         self._cards[1].rank == self._cards[2].rank-1 and \
         self._cards[2].rank == self._cards[3].rank-1 and \
         self._cards[3].rank == self._cards[4].rank-1:

          self.hand_type = STRAIGHT

        elif self._cards[0] == self._cards[1] and \
         self._cards[1] == self._cards[2]:

          self.hand_type = THREE_OF_A_KIND

        elif self._cards[1] == self._cards[2] and \
         self._cards[2] == self._cards[3]:

          self.hand_type = THREE_OF_A_KIND
    
        elif self._cards[2] == self._cards[3] and \
         self._cards[3] == self._cards[4]:

          self.hand_type = THREE_OF_A_KIND

        elif self._cards[0] == self._cards[1] and \
         self._cards[2] == self._cards[3]:
    
          self.hand_type = TWO_PAIR
        
        elif self._cards[0] == self._cards[1] and \
         self._cards[3] == self._cards[4]:
    
          self.hand_type = TWO_PAIR
    
        elif self._cards[1] == self._cards[2] and \
         self._cards[3] == self._cards[4]:
    
         self.hand_type = TWO_PAIR

        elif self._cards[0] == self._cards[1]:
    
         self.hand_type = ONE_PAIR
    
        elif self._cards[1] == self._cards[2]:
        
         self.hand_type = ONE_PAIR

        elif self._cards[2] == self._cards[3]:
        
         self.hand_type = ONE_PAIR

        elif self._cards[3] == self._cards[4]:
        
         self.hand_type = ONE_PAIR

        elif self._cards[0] != self._cards[1] and \
         self._cards[1] !=  self._cards[2] and \
         self._cards[2] != self._cards[3] and \
         self._cards[3] !=  self._cards[4]:
          
          self.hand_type = NO_PAIR