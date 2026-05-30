
# game guess number.

import random

def play_game():
    game_count = 0
    wins_count = 0
    losses_count = 0
    computer=random.choice([1, 2, 3])
    def rounds(name):
        try:
             
         while True:
            nonlocal wins_count
            nonlocal losses_count

            print (f"hello! {name}, welcone to this game named: \n guess the number. \nso which number i was thinking about.")

            user = float(input("was it...., \n 1, \n 2, \n or 3\n "))


            
            # while True:
                
            #     if users not in choice["1,2,3"]: # blackets and each defined 
            #         print(f"\nplease choose between 1,2,3 ")
            #         return rounds(name) # for avoiding the upper number
            #     else:
            #         break
            if user >= 4: # after this long time i set the boundary to the user choice input
                print("only from 1 up to 3 is allowed. ")
                return rounds(name)
            print(f"{name} you chose {user}")
            print(f"i was thinking about {computer}")
            if user == computer:
                wins_count += 1
                print(f"{name} you win!")
            elif user != computer:
                losses_count += 1
                print(f"{name} you lost!")

            nonlocal game_count
            game_count += 1
            print(f"game_count: {game_count} \nwins_count: {wins_count} \n losses_count: {losses_count} \n want to playagain?\n")
        
            print("")
            while True:
                playagain = input("\n y for yes, \n n for no \n")

                if playagain not in ("y,n"): # separate condition to continue
                    print(f"please chose between y or n \n")
                    continue # continue the choice section
                else:  # this is the repeat flow.
                    break

            if playagain == "y": # levels to the loop to stop it  after the inner succeed
                    return rounds(name)
            else:
                print("thanks for playing!. ")
                break
        except ValueError:
            print(f" hey! only numbers between 1,2 and 3 are alowed")
            return rounds(name)
    if __name__ == "__main__":
        import argparse
        parser = argparse.ArgumentParser(
            description="greetings to the player!"
        )
        parser.add_argument(
            "-n","--name", metavar="name",
            required=True, help="put in the name of a player. "
        )
        args = parser.parse_args()
        rounds(args.name)
play_game()
    