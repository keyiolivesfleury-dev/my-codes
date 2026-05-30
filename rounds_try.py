# this game lets you guess the number that computer has chosen with in the range of 1 to 100

import random
# import sys
def lap_up():
    attempts_count = 0
    count_loses = 0
    wins_count = 0 
    computer = random.randint(1,100)# randint when dealing with range stuff
    print("hello! welcome to this game.\nnamed guess computer's choice! \nlet's start!")
    def rounds():
           while True: 
                nonlocal attempts_count
                attempts_count += 1
                nonlocal count_loses
                count_loses += 1
                nonlocal wins_count
                try:
                    
                    userchoice = float(input("\nwhich one is it?: "))
                    user = float(userchoice)
                    # if not type(user) is float:
                    #     raise ValueError("only numbers are allowed") 
                
                    print(f"\nyou chose {user}")
                    if user > computer:
                        print("\nthat's higher!, try the lower one!\n ")
                        return rounds()
                    elif user < computer:
                        print("\n that's lower!, try the higher one!\n ")
                        return rounds()
                    else:
                        wins_count += 1 # we increment exactly where we want to add our counts.we wanted to count the wins so it must be here.
                        print(f"\n you have won!🍾🍾🍾, \n computer number was:{computer} \n ")
                        print(f"attempts_counts: {attempts_count} \n count_loses: {count_loses} \n wins_count: {wins_count} \n \n want to play again?")
                    
                
                    play_again = str(input(f"choose y for yes or n for no \n" ))
                    if play_again not in ("y,n"):
                        print("please choose between y and n")
                    elif play_again == "y":
                        return rounds()
                    else:
                        print("thanks for playing our game! \n bye bye!👋👋")
                        break
                
                except ValueError: # this calls out the datatypes errors
                    print(f"\n an error have occoured! \n only numbers are allowed \n please try again. ")
    rounds() # while true calls the rounds
            
lap_up()        