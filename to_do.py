"""
this simple program is a to do list that allows you to add, remove, and view tasks. it saves the tasks to a file so that you can access them later.
"""


#this is the way i firstly open the file.

# f = open("daily_activities.txt","w")
# # print(f.read())
# f.close()
import sys 

def to_do():

    print("\ngreetings! let me help you with the tasks.")

to_do()


def choices():

    while True: # this has to be inside the function so that it can  run!
        try:
                    
                # user choice
                    print('')
                    
                    choice = int(input("\nchoose:\n1 for adding\n2 for removing\nand 3 for review the task.\n"))
        
                    
                    if choice >= 4:
                        print("that option is not available,\nonly choose from 1 up to 3.")
                        continue 
                    if choice == 0:
                        print("that is out of choice list!")
                        continue
                    if choice == 1:      
                        new_task = input("insert what you want to add: \n")
                        with open ("daily_activities.txt","a") as f:
                            print('')
                            f.write("\n")
                            f.write(new_task)
                            
                            print("\nyour task has been successfully added!.\n")

                    # removing things from a file.

                    elif choice == 2:
                        # make a file into a list.
                            new_task2 = input("\ntype what you want to remove from the todo list: \n")
                            with open ("daily_activities.txt","r") as f:
                                tasks = f.readlines()

                                # remove a task from the list 
                                found = False # variable to check if the task is found or not
                                for task in tasks:
                                    if task.strip() == new_task2: # when they match
                                        tasks.remove(task)
                                        found = True
                                        break

                                if found:
                                        with open("daily_activities.txt", "w") as f:
                                            f.writelines(tasks)
                                            print("\nthe task has been successfully removed!\n")
                                else: # if value not found
                                        print("the task doesn't exist yet!")
                            
                            
                    else:
                        print("\ncool then your schedule looks like this: ")
                        with open ("daily_activities.txt","r") as f:
                            context = f.read()
                            print('')
                            print(context)
                        
                            print('')
                    
                    
                
                    
                    again = input("want to keep on with the tasks?\nchoose:\ny for yes.\nn for no.\n")
                    if again == "y":
                        print("\nokay! let's do it, again!")
                        continue 
                    elif again not in "n,y":
                        print("only y and n are the choices!")

                        
                    else:
                        print("\nthanks! for using our app!\ngoodbye👋👋👋👋\n")
                        # break ( this can work but i want the system.exit() to be used here.)
                        sys.exit() # this kills the whole program and exits the loop.
        except ValueError:
                    print("hey only numbers, are allowed!")
                    continue
                        
choices()

        

        





