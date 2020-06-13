# Armando Oritz
# Project 2
# April - 24 - 2019
def frame_score(the_frame, bonus1, bonus2):
    # Case where frame is a strike
    if the_frame[0] == 10:
        return 10 + bonus1 + bonus2   
    # Case where frame is a spare
    elif the_frame[0] + the_frame[1] == 10:
        return 10 + bonus1    
    # Case where frame is an open frame
    else:
        return the_frame[0] + the_frame[1]