# Armando Oritz
# Project 2
# April - 24 - 2019
from framescore import frame_score
from raggedarray import read_ragged_array

input_file = input("Enter file name:")
frames = read_ragged_array(input_file)
ragged_array = frames
score = 0
for i in range(1, 11):  
    if frames[i][0] ==10 and frames[i+1][0]==10:
        bonus1 = 10
        bonus2 = frames[i+2][0]
    elif frames[i][0] == 10 and frames[i+1][0] < 10:
      bonus1 = frames[i+1][0]
      bonus2 = frames[i+1][1] 
    elif frames[i][0] + frames[i][1] == 10:
      bonus1 = frames[i+1][0] 
      bonus2 = 0
    else:
      bonus1 = 0
      bonus2 = 0
    score += frame_score(frames[i], bonus1, bonus2)
print(score)