import random
# Armando Oritz
# Project 2b enhanced Rock-Paper-Scissors-Lizard-Spock
# Due Date : 1/31/19
# Submission Date : 1/30/19

human_score = 0.0
computer_score = 0.0 

plays = ["rock", "paper", "scissors", "spock", "lizard"]

while True:
    human_play = input("Input Human Play: ")
    computer_play = random.choice(plays)
    
    if  human_play == computer_play:
        print("Tie!")
        human_score = human_score + .5
        computer_score = computer_score +.5

    elif human_play == "rock" and computer_play =="paper":
        print("Paper covers Rock")
        print("Computer Wins")
        human_score = computer_score + 1
    elif human_play == "rock" and computer_play =="spock":
        print("Spock vaporizes Rock")
        print("Computer Wins")
        human_score = computer_score + 1    
    elif human_play == "rock" and computer_play =="scissors":
        print("Rock crushes Scissors")
        print("Human Wins")
        human_score = human_score + 1
    elif human_play == "rock" and computer_play =="lizard":
        print("Rock crushes lizard")
        print("Human Wins")
        human_score = human_score + 1    

    elif human_play == "paper" and computer_play =="scissors":
        print("Scissors cuts Paper")
        print("Computer Wins")
        computer_score = computer_score +1
    elif human_play == "paper" and computer_play =="lizard":
        print("Lizard eats Paper")
        print("Computer Wins")
        computer_score = computer_score +1
    elif human_play == "paper" and computer_play =="spock":
        print("Paper disproves Spock")
        print("Human Wins")
        human_score = human_score + 1
    elif human_play == "paper" and computer_play =="rock":
        print("Paper covers Rock")
        print("Human Wins")
        human_score = human_score + 1

    elif human_play == "scissors" and computer_play =="rock":
        print("Rock crushes Scissors")
        print("Computer Wins")
        computer_score = computer_score +1
    elif human_play == "scissors" and computer_play =="paper":
        print("Scissors cut Paper")
        print("Human Wins")
        human_score = human_score + 1 
    elif human_play == "scissors" and computer_play =="lizard":
        print("Scissors decapitates Lizard")
        print("Human Wins")
        human_score = human_score + 1 
    elif human_play == "scissors" and computer_play =="spock":
        print("Spock smashes Scissors")
        print("Computer Wins")
        computer_score = computer_score +1

    elif human_play == "spock" and computer_play =="lizard":
        print("Lizard poisons Spock")
        print("Computer Wins")
        computer_score = computer_score +1
    elif human_play == "spock" and computer_play =="scissors":
        print("Spock smashes Scissors")
        print("Human Wins")
        human_score = human_score + 1 
    elif human_play == "spock" and computer_play =="rock":
        print("Spock Vaporizes Rock")
        print("Human Wins")
        human_score = human_score + 1 
    elif human_play == "spock" and computer_play =="paper":
        print("Paper disproves Spock")
        print("Computer Wins")
        computer_score = computer_score +1

    elif human_play == "lizard" and computer_play =="scissors":
        print("Scissors decapitates Lizard")
        print("Computer Wins")
        computer_score = computer_score +1
    elif human_play == "lizard" and computer_play =="rock":
        print("Rock crushes Lizard")
        print("Computer Wins")
        computer_score = computer_score +1
    elif human_play == "lizard" and computer_play =="spock":
        print("Lizard poisons Spock")
        print("Human Wins")
        human_score = human_score + 1
    elif human_play == "lizard" and computer_play =="paper":
        print("Lizard eats Paper")
        print("Human Wins")
        human_score = human_score + 1

    print(human_score, computer_score)
