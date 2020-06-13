# Armando Oritz
# Project 3
# Due Date: 2/7/19
# Submission Date : 2/6/19

# Input first and last name to look up a name and credit hours and grade points are intialized
desired_firstname = input ("Enter first name: ")
desired_lastname = input ("Enter last name: ")
total_credithours = 0.0
total_gradepoints = 0.0
#file called fin opened and read
fin = open ("grade-records.txt" , "r")
#first line ignored and second line read
fin.readline()
line = fin.readline() 
#while loop to run through file as long as it is not empty using the fields
while line != "":
    fields = line.split(",")
    last_name = fields[1].strip( )
    first_name = fields[2].strip( )
    credit_hours = int(fields[6].strip( ))
    grade = fields[7].strip( )
#if statements to determine gpa of gpa of the desired first and last name
    if(first_name == desired_firstname and last_name == desired_lastname):
        if(grade == "A"):
            grade_points = credit_hours * 4
        elif(grade == "B"):
            grade_points = credit_hours * 3
        elif(grade == "C"):
            grade_points = credit_hours * 2
        elif(grade == "D"):
            grade_points = credit_hours * 1
        else:
            credit_hours = credit_hours * 0
        total_credithours = total_credithours + credit_hours
        total_gradepoints = total_gradepoints + grade_points
    line = fin.readline()
fin.close( )
#gpa is calculated and printed out 
gpa = total_gradepoints / total_credithours
print(f"GPA for {desired_firstname} {desired_lastname} is {round(gpa, 2)}.")        
        
