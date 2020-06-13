# Armando Ortiz
# Project 5
# 6-6-19

from cardb import Card
from pokerhand import PokerHand
from constants import *
import unittest
# Case where four of a kind < kicker.
class MyUnitTestClass(unittest.TestCase):
    def test_1(self):
        arr = [ Card(9, "C"), Card(9, "S"),
            Card(9, "H"), Card(9, "D"),
            Card(11, "S") ]
        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, FOUR_OF_A_KIND)

    # Case where four of a kind > kicker.
    def test_2(self):
        arr = [ Card(3, "S"), Card(13, "C"), 
            Card(13, "S"), Card(13, "H"), 
            Card(13, "D") ]
        
        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, FOUR_OF_A_KIND)
    # test straight flush 
    def test_3(self):
        arr = [ Card(3, "S"), Card(4, "S"), 
            Card(6, "S"), Card(5, "S"), 
            Card(7, "S") ]
        
        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, STRAIGHT_FLUSH)
    # test full house with lower pair
    def test_4(self):
        arr = [ Card(3, "S"), Card(13, "C"), 
            Card(3, "S"), Card(13, "H"), 
            Card(13, "D") ]
        
        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, FULL_HOUSE)
    # test full house with higher pair
    def test_5(self):
        arr = [ Card(4, "S"), Card(4, "C"), 
            Card(4, "S"), Card(13, "H"), 
            Card(13, "D") ]
      
        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, FULL_HOUSE)
    # test flush 
    def test_6(self):
        arr = [ Card(3, "S"), Card(13, "S"), 
        Card(10, "S"), Card(12, "S"), 
        Card(4, "S") ]
        
        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, FLUSH)
    # test straight 
    def test_7(self):
        arr = [ Card(3, "S"), Card(4, "C"), 
        Card(5, "S"), Card(7, "H"), 
        Card(6, "D") ]
        
        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, STRAIGHT)
    # test lower three of a kind
    def test_8(self):
        arr = [ Card(3, "S"), Card(3, "C"), 
        Card(3, "S"), Card(13, "H"), 
        Card(12, "D") ]
        
        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, THREE_OF_A_KIND)
    # test middle three of a kind
    def test_9(self):
        arr = [ Card(3, "S"), Card(13, "C"), 
        Card(4, "S"), Card(4, "H"), 
        Card(4, "D") ]
        
        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, THREE_OF_A_KIND)
    # test higher three of a kind
    def test_10(self):
        arr = [ Card(3, "S"), Card(4, "C"), 
        Card(13, "S"), Card(13, "H"), 
        Card(13, "D") ]
        
        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, THREE_OF_A_KIND)
    # test 1,1,1,1,0 two pair
    def test_11(self):
        arr = [ Card(3, "S"), Card(3, "C"), 
        Card(4, "S"), Card(4, "H"), 
        Card(13, "D") ]
        
        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, TWO_PAIR)
    # test 1,1,0,1,1 two pair
    def test_12(self):
        arr = [ Card(3, "S"), Card(3, "C"), 
        Card(4, "S"), Card(5, "H"), 
        Card(5, "D") ]
        
        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, TWO_PAIR)
    # test 0,1,1,1,1 two pair
    def test_13(self):
        arr = [ Card(3, "S"), Card(4, "C"), 
        Card(4, "S"), Card(9, "H"), 
        Card(9, "D") ]
        
        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, TWO_PAIR)
    # test 1,1,0,0,0 one pair
    def test_14(self):
        arr = [ Card(3, "S"), Card(3, "C"), 
        Card(4, "S"), Card(7, "H"), 
        Card(10, "D") ]
        
        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, ONE_PAIR)
    # test 0,1,1,0,0 one pair
    def test_15(self):
        arr = [ Card(3, "S"), Card(4, "C"), 
        Card(4, "S"), Card(7, "H"), 
        Card(10, "D") ]
        
        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, ONE_PAIR)
    # test 0,0,1,1,0 one pair
    def test_16(self):
        arr = [ Card(2, "S"), Card(3, "C"), 
        Card(4, "S"), Card(4, "H"), 
        Card(10, "D") ]
        
        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, ONE_PAIR)
    # 0,0,0,1,1 one pair
    def test_17(self):
        arr = [ Card(2, "S"), Card(3, "C"), 
        Card(4, "S"), Card(7, "H"), 
        Card(7, "D") ]
        
        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, ONE_PAIR)
    # test no pair 
    def test_18(self):
        arr = [ Card(2, "S"), Card(5, "C"), 
        Card(6, "S"), Card(9, "H"), 
        Card(11, "D") ]
        
        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, NO_PAIR)


if __name__ == '__main__':
    unittest.main( )
