# Armando Ortiz
# Project 4b
# 5-22-19
from onlinestudent import Onlinestudent

#creates student and test __str__ method 
o = Onlinestudent("1111", "Carter", "Marilyn", "312/473-4837", 1,"mcarter@coolmail.net")
print(o)
#test email variable
print(o.email)
#test __lt__ method
o1 = Onlinestudent("1111","Graber","Gary","312/837-2837",3,"ggraber@coolmail.net")
o2 = Onlinestudent("1112","Cheng","Sam","312/272-4473",1,"scheng@coolmail.net")
print(o1 < o2)
#test study_group variable
print(o.study_group)
#test add_group_member
o.add_group_member(1113)
print(o.study_group)
# test __repr__ method 
print(repr(o))