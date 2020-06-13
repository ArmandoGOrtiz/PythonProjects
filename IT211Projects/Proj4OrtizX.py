# Armando Oritz
# Project 4
# Due Date: 2/17/19
# Submission Date : 2/19/19

# Draw the letter Z using asterisks

# Open output file
fout = open("z.txt", "w")

# Draw diagonal lines 
for y in range(0, 18):
    for x in range(14, 20 + y):
        fout.write(" ")
    for x in range(7, 13):
        fout.write("*")
    fout.write("\n")
    for x in range(0, 19 - y):
        fout.write(" ")
    for x in range(1, 7):
        fout.write("*")
    fout.write("\n")

# Close output file
fout.close( )