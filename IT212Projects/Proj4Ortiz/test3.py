# Armando Ortiz
# Project 4c
# 5-27-19

from onlinestudent import Onlinestudent

students = []
fin = open("student.txt","r")
#goes through student.txt and creates a list of online students and organized by username in alphabetical order
for line in fin:
    fields = line.split(",")
    username_test = fields[0]
    lastname_test = fields[1]
    firstname_test = fields[2]
    phone_test = fields[3]
    year_test = fields[4]
    email_test = fields[5]
    os = Onlinestudent(username_test,lastname_test,firstname_test,phone_test,int(year_test),email_test)
    students.append(os)
fin.close()
students.sort(key=lambda x: x.username)
print([item.username for item in students])

# goes through study-groups.txt and creates a list of study groups 
fin = open("study-groups.txt","r")
for line in fin:
    fields = line.split(",")
    for s in students:
        if s.username == fields[0]:
            for i in range(1,len(fields)):
                s.study_group.append(fields[i])

#prints the online students details and username
for s in students:
    print(s)
    print(s.username,"\n")

#input the username and find out what group members they have
request = input("Enter student username: ")
for s in students:
    if request == s.username:
        print(s)
        for t in s.study_group:
            print(t)
fin.close()
