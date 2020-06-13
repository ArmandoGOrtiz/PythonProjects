# Armando Oritz
# Project 1
# Due Date : 1/17/19
# Submission Date : 1/14/19

p = float(input(" Enter Amount of Loan: "))
if(p >= 0 ):
    r = float(input("Interest rate in percentage: "))
    if(r>=0):
        n = float(input("Number of Years: ")) 
        if(n>=0):

            t = (p * r /1200)
            b = 1-(1+r/1200)**(-12 * n)

            m = t / b
            print("Your Monthly Payment is ", round(m,2), "$")
        else:
            print("No Negative Integers! ")
    else:
        print("No Negative Integers! ")
else:
    print("No Negative Integers! ")