# Armando Ortiz
# Lab 2
# 4-26-19


from clock import Clock
import unittest

class MyUnitTestClass(unittest.TestCase):
        
    def test_1(self):
        c = Clock(4, 7, 3)
        self.assertEqual(str(c), "04:07:03")
        self.assertEqual(c.hour,4)
        self.assertEqual(c.minute,7)
        self.assertEqual(c.second,3)   
        c.tick()
        self.assertEqual(str(c), "04:07:04")
    
    def test_2(self):
        c2 = Clock(4, 7, 59)
        self.assertEqual(str(c2), "04:07:59")
        c2.tick( )
        self.assertEqual(str(c2), "04:08:00")
         
    def test_3(self):
        c3 = Clock(4, 59, 59)
        self.assertEqual(str(c3), "04:59:59")
        c3.tick( )
        self.assertEqual(str(c3), "05:00:00")

    def test_4(self):
        c4 = Clock(23, 59, 59)
        self.assertEqual(str(c4), "23:59:59")
        c4.tick( )
        self.assertEqual(str(c4), "00:00:00")


if __name__ == '__main__':
    unittest.main( )