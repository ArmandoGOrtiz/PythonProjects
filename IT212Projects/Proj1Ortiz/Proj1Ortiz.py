a = 0x39
b = 0x7b 
c = a & b
d = a | b
e = a ^ b
# question 4
print(c)
print(d)
print(e)
# d is decimil 02 if field with 2 and 08 is field with 8 b is binary x in hex
print("{0:d}; {1:02x}; {2:08b}".format(c,c,c))    
print("{0:d}; {1:02x}; {2:08b}".format(d,d,d))
print("{0:d}; {1:02x}; {2:08b}".format(e,e,e))