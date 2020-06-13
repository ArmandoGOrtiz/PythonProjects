# Armando Ortiz
# Lab 2
# 4-26-19


class Clock:

    # __init__ method is called whenever a new clock 
    # object is created.
    def __init__(self, the_hr, the_min, the_sec):
        self.hour = the_hr
        self.minute = the_min
        self.second = the_sec

    # Regular method.
    def tick(self):
        self.second += 1
        if self.second >= 60:
            self.second = 0
            self.minute += 1
        if self.minute >= 60:
            self.minute = 0
            self.hour += 1
        if self.hour >= 24:
            self.hour = 0
            self.minute = 0
            self.second = 0

    # Define return value for str method.
    def __str__(self):
        return "{0:02d}:{1:02d}:{2:02d}".format(self.hour, self.minute , self.second)