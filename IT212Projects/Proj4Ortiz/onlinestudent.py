# Armando Ortiz
# Project 4b
# 5-22-19

from student import Student

class Onlinestudent(Student):
    def __init__(self, the_username, the_lastname, the_firstname, the_phone, the_year,the_email):
        self.username = the_username
        self.lastname = the_lastname
        self.firstname = the_firstname
        self.phone = the_phone
        self.email = the_email
        self.study_group = []
        self.year = the_year
        if self.year < 1:
            self.year = 1
        elif self.year > 4:
            self.year = 4
        else:
            self.year = self.year
    #__str__method format string   
    def __str__(self):
        return super( ).__str__( ) + f" {self.email}"

    def __repr__(self):
        return str(self)
    
    def __lt__(self,other):
        if self.username < other.username:
            return True

    def add_group_member(self, member_id):
        self.member = int(member_id)
        self.study_group.append(self.member)
