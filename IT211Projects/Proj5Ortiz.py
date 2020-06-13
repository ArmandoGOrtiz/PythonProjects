# Armando Oritz
# Project 5
# Due Date: 3/1/19
# Submission Date : 2/28/19

#example type bbya 
#output: 
#abby
#baby

import itertools 
def get_permutations():
    #Enter Jumble string then get array of all permuations
    word_input = input("Enter the jumbled string: ")
    letters = list(word_input)
    permutation_list = itertools.permutations(letters)
    permutations = [ ]
    for perm in permutation_list:
        permutations.append(''.join(perm))
    #open file then read first line
    fin = open("dict.txt" , "r" )
    line = fin.readline()
    #as long as line is not empty go through loop
    while line != "":
        #strip line of \n and make it lower case
        line =line.strip()
        line =line.lower()
        if(line[0]==line[0].lower()):
            #p is all the permuations in the array
            for p in permutations:
                if(p==line):
                    #if permuation is = to a word print it
                    print(p)
                    break  
        line = fin.readline()     
    fin.close()  
get_permutations()