# Armando Oritz
# Project 4
# Due Date: 2/17/19
# Submission Date : 2/19/19

# Draw the letter H using asterisks , works horizontally , builds on from previous 

# Open output file
fout = open("L.txt", "w")

# Draw top 
for y in range(0, 12):
    for x in range(0, 6):
        fout.write("*")
    fout.write("\n")

#bottom Horizontal
for y in range(0, 3):
    for x in range(0, 30):
        fout.write("*")
    fout.write("\n")

# Close output file.
fout.close( )