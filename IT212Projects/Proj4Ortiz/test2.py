# Armando Ortiz
# Project 4b
# 5-22-19

from onlinestudent import Onlinestudent
import unittest

class MyUnitTestClass(unittest.TestCase):
    # test __str__ and __init__ methods and all variables
    def test_1(self):
        o = Onlinestudent("1111", "Carter", "Marilyn", "312/473-4837", 1,"mcarter@coolmail.net")
        self.assertEqual(str(o),"1111;Carter;Marilyn;312/473-4837;1 mcarter@coolmail.net")
        self.assertEqual(o.username,"1111")
        self.assertEqual(o.lastname,"Carter")
        self.assertEqual(o.firstname,"Marilyn")   
        self.assertEqual(o.phone,"312/473-4837")
        self.assertEqual(o.year,1)
        self.assertEqual(o.email,"mcarter@coolmail.net")
    # test 2 __repr__ method
    def test_2(self):
        o = Onlinestudent("1111", "Carter", "Marilyn", "312/473-4837", 1,"mcarter@coolmail.net")
        o.__repr__()
        self.assertEqual(str(o), "1111;Carter;Marilyn;312/473-4837;1 mcarter@coolmail.net")
    # test 3 __lt__ method
    def test_3(self):
        o1 = Onlinestudent("1111","Graber","Gary","312/837-2837",3,"ggraber@coolmail.net")
        o2 = Onlinestudent("1112","Cheng","Sam","312/272-4473",1,"scheng@coolmail.net")
        self.assertEqual(str(o1 < o2), "True")
    # test 4 study_group list
    def test_4(self):
        o = Onlinestudent("1111", "Carter", "Marilyn", "312/473-4837", 1,"mcarter@coolmail.net")
        self.assertEqual(str(o.study_group), "[1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120]")
    # test 5 add_group_member
    def test_5(self):
        o = Onlinestudent("1111", "Carter", "Marilyn", "312/473-4837", 1,"mcarter@coolmail.net")
        o.add_group_member(1113)
        self.assertEqual(str(o.study_group), "[1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1113]")
if __name__ == '__main__':
    unittest.main( )