'''
Wokflow of Project
1.Input from user(Rock,paper,scissor)
2.Computer choice (Computer will choses randomly not coditinally)
3.Result print


#Cases
A-Rock
Rock - Rock = tie
Rock - Paper = Paper Win
Rock - scissor = Rock wine

B -Paper
Paper - Paper = tie
Paper - Rock = Paper Win
Paper - Scissor = Scissor

C - Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win


'''
import random

while True:
    list_item = ["Rock","Paper","Scissor"]
    user_choice = input("Enter your choice -Rock-Paper-Scissor__")
    com_choicce = random.choice(list_item)
    
    print(f"Your choice is {user_choice} and Com choice - {com_choicce}")
    
    if user_choice == com_choicce:
        print("Both choice are same the game is tie..")
    elif user_choice == "Rock":
        if com_choicce == "Paper":
            print("Winner is Com")
        elif com_choicce == "Scissor":
            print("You are winner")
    elif user_choice == "Paper":
        if com_choicce == "Rock":
            print("You are winner.")
        else:
            print("Winner is Com")
    elif user_choice == "Scissor":
        if com_choicce == "Rock":
            print("Winner is Com")
        else:
            print("You are winner.")
    else:
        print('Please Enter the correct choice..')