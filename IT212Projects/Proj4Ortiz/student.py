# Armando Ortiz
# Project 4a
# 5-15-19

class Student:
    #__init__ method with using if statement to check year
    def __init__(self, the_username, the_lastname, the_firstname, the_phone, the_year):
        self.username = the_username
        self.lastname = the_lastname
        self.firstname = the_firstname
        self.phone = the_phone
        self.year = the_year
        if self.year < 1:
            self.year = 1
        elif self.year > 4:
            self.year = 4
        else:
            self.year = self.year
    #__str__method format string   
    def __str__(self):
        return f"{self.username};{self.lastname};{self.firstname};{self.phone};{self.year}"

    def __repr__(self):
        return str(self)
    #update year by + 1
    def update_year(self):
        if self.year < 4:
            self.year += 1