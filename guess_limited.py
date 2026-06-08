""" this game is a bit different from the others because it gives a user a specfic attempts numbers and count them the scores.
"""

import random

def game(name):# i was not sure that this argparse is going to work twice! but it did
    
    scores = 0
    attempts = 0
    
    print(f"\nhello, {name}!how are u? \nwelcome to this game \n named keyi_games \nready to start?.\n")
    print(f"then guess a number that is in my mind btn 1&10 \n")
    def limits(name):
       
        nonlocal attempts
        
        nonlocal scores
        
        computer = random.randint(1,10) # this choice must stay out of the while to select the other not the same as the last one.
        while True:
            try:
                
                user = float(input(f"so it is?: \n"))
                if user >= 11:
                    print(f" ohh {name} choose between 1 and 10!")
                    continue
                
                if user != computer:
                    attempts += 1 # it don't count the last number both attempts and win!! why??
                   
                    if attempts >= 4: # if from the first line.
                        print(f"you've lost. \nno attempts left.\n\n my number was: {computer} \nyou tried: {attempts} times\nscores: {scores}")
                        return game(name)
                    print("please try again.")
                    # break # this was not employing the playagain
                    return limits(name)
               
                elif user == computer: # it is still jumping some numbers that are equal to it! why?
                    
                    scores += 1
                    print(f"{name} you have won! \n my number was: {computer}  \nyou tried: {attempts} times\nscores: {scores} ")
                
                
                
               
                playagain = input(f"enter y for yes \n or n for no. \n")
                if playagain not in ("y,n"):
                     print(f"{name} please choose between y and n!")
                elif  playagain == "y":
                     print(f"\nokay {name} let's continue")
                     #return limits(name)# this is not working because it is like keeping the loop.
                     return game(name)
                elif playagain == "n":
                     print(f"{name} it was a pleasure to play with you! \n good_bye👋👋👋")
                     break
            except ValueError:
                 print(f"{name} only numbers are allowed! \n from 1 up to 10")
     
    if __name__ == "__main__":
        import argparse
        parser = argparse.ArgumentParser(
            description="help to the player"
        )
        parser.add_argument(
            "-n","--name", metavar="name",
            required=True,help="please enter your name"
        ) # i left out - to "-name" and the system collapsed( they must be 2 --) 
        args = parser.parse_args()
        limits(args.name)
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="help to the player"
    )
    parser.add_argument(
        "-n","--name", metavar="name",
        required=True,help="please enter your name"
    ) 
    args = parser.parse_args()
    game(args.name)
    

                     
                

        
