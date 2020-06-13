# Armando Ortiz
# Project 3a
# 5-2-19

#from card.py import card class and import unittest
from card import Card
import unittest

class MyUnitTestClass(unittest.TestCase):
    # test 1 test Deck
    def test_1(self):
        d = Deck()
        self.assertEqual(str(d),"Deck object")
    # test 2 test Deal
    def test_2(self):
        d = Deck( )
        c = d.deal( )
        self.assertEqual(str(c), "AS")
        self.assertEqual(d.count( ), 51)
        print(d.count( ))  
    # test 3 add_to_bottom
    def test_3(self):
        d = Deck()
        c = d.add_to_bottom( )
        self.assertEqual(str(c), "AS")
    # test 4 add_to_top
    def test_4(self):
        d = Deck()
        c = d.add_to_top( )
        self.assertEqual(str(c), "AS")
    # test 5 is_empty
    def test_5(self):
        d = Deck()
        c = d.is_empty( )
        self.assertEqual(str(c), "False")      

if __name__ == '__main__':
    unittest.main( )