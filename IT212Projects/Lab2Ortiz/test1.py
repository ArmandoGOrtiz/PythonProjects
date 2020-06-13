# Armando Ortiz
# Lab 2
# 4-26-19


from clock import Clock
c = Clock(4, 7, 3)
print(c.hour, c.minute, c.second)
c.tick()
print(c)

c2 = Clock(4,7,59)
c2.tick()
print(c2)

c3 = Clock(4,59,59)
c3.tick()
print(c3)

c4 = Clock(23,59,59)
c4.tick()
print(c4)