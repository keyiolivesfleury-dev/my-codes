""" this is the program that will generate a password for a user and will also recognize it if they need it again"""

import random
import string 
import secrets


def welcome():
    print("\nwelcome to the password generator!\n")
    print("this program will generate a password for you and will also recognize it if you need it again.\n")
    print("please follow the instructions below to generate your password.\n")

welcome()


def password():
    while True:
       
      try:
        
        length = int(input(" please choose a password length: \n"))


        print("\nyour password is:")
        password = ''.join(secrets.choice(
            string.ascii_letters +
            string.digits + 
            string.punctuation) 
              for i in range(length)) #looping throuht the length of the password and generate the random.

        print(password)
        break # for stoping the loop if the password is generated successfully
        

      except ValueError:
        print("\nno letters are allowed, only numbers are allowed\n")
        continue
          
password()


def again():
    
    while True:
      try:
         
        print("\nwant to generate again?\n")  
        again = input("y for yes\nor n for no.\n")
        if again == "y":
            password() # this calls the password function again,and it is better than the return statement( this kills the program and ends it at the second attempt).
            
        elif again not in "y , n":
          print("\nthat is not y or n!")
          continue
        else:
          print("\nthanks for using our service!" )
          break 

      except ValueError:
         print("no numbers are allowed")
         continue 
      
again()
