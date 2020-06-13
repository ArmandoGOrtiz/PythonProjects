# Armando Oritz
# Project 6
# Due Date: 3/12/19
# Submission Date : 3/11/19
import os 
import shutil
previous_album = ""
#open file index and reading the lines
fin = open("index.txt", "r")
line = fin.readline()
# while line is not empty assign first field to folder_name,and second field to original_photo_name
while line != "":
    line = line.strip()
    fields = line.split(",")
    folder_name = fields[0]
    original_photo_name = fields[1]
    # if previous album is not equal to folder name create folder and assign previous_album to folder_name
    if previous_album != folder_name:
        os.makedirs(folder_name)
        counter = 1
        previous_album = folder_name
        print("Creating folder " + folder_name)
    print("Putting " + original_photo_name + " in folder " + folder_name)
    new_photo_name = "{:s}/{:03d}-{:s}". \
    format(folder_name, counter, original_photo_name)
    shutil.copy("originals/" + original_photo_name , new_photo_name)
    counter += 1
    line = fin.readline()