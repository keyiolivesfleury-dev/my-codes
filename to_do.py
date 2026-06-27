"""
this simple program is a to do list that allows you to add, remove, and view tasks. it saves the tasks to a file so that you can access them later.
"""


#this is the way i firstly open the file.

# f = open("daily_activities.txt","w")
# # print(f.read())
# f.close()


def to_do():

    print("\ngreetings! let me help you with the tasks.")
    try:


        def choices():
                
        # user choice
            print('')
            
            choice = int(input("\nchoose:\n1 for adding\n2 for removing\nand 3 for review the task.\n"))

            # adding things to a file
            
            if choice >= 5:
                print("that option is not available,\nonly choose from 1 up to 4.")
                return choices()
            if choice == 0:
                print("that is out of choice list!")
                return choices()
            if choice == 1:      
                new_task = input("insert what you want to add: \n")
                with open ("daily_activities.txt","a") as f:
                    print('')
                    f.write("\n")
                    f.write(new_task)
                    f.close()
                    print("\nyour task has been successfully added!.\n")

            # removing things from a file.

            elif choice == 2:
                # make a file into a list.
                    new_task2 = input("\ntype what you want to remove from the todo list: \n")
                    with open ("daily_activities.txt","r") as f:
                        tasks = f.readlines()
                        # remove a task from the list 
                        for task in tasks:
                            if task.strip() == new_task2: # when they match
                                tasks.remove(task)
                                break 

                        for task in tasks:
                            if task.strip() != new_task2:
                                
                                print("\nthat task doesn't exist yet!.\ni'm afraid we will have to start again.")
                                return choices()


                    with open ("daily_activities.txt","w") as f:
                        f.writelines(tasks)
                        print("\nnow your task is removed.\n")
            else:
                print("\ncool then your schedule looks like this: ")
                with open ("daily_activities.txt","r") as f:
                    context = f.read()
                    print('')
                    print(context)
                    f.close()
                    print('')

            def new():
                again = input("want to keep on with the tasks?\nchoose:\ny for yes.\nn for no.\n")
                if again == "y":
                    print("\nokay! let's do it, again!")
                    return choices()
                elif again == "n":
                    print("\nthanks! for using our app!\ngoodbye👋👋👋👋\n")
                    return
                else:
                    print("only y and n are choices!\n")
                    return new()
            new()

        choices()
            
    except ValueError:
            print("hey only numbers!")
            return choices() # this def must be inside the try tree to be called!

         
to_do()




