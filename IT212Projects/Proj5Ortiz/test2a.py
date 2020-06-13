# Armando Ortiz
# Project 5
# 6-6-19

#from card.py import card class and import unittest
from cardb import Card
from pokerhand import PokerHand
from constants import *
import unittest

class MyUnitTestClass(unittest.TestCase):
    # test 1 test the __lt__ method 
    def test_1(self):
        c = Card(4,"S")
        c2 = Card(3,"S")
        c3 = [c,c2]
        c3.sort()
        c4 = [Card(3,"S"),Card(4,"S")]
        self.assertEqual(c3,c4)
    # test 2 test __eq__ method
    def test_2(self):
        c = Card(3,"S")
        c2 = Card(3,"S")
        self.assertEqual(c,c2)

if __name__ == '__main__':
    unittest.main( )