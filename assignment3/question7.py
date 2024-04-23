# Assignment 3 Question 7

import bcrypt
import pwinput

# prompt user with options

selected_option = int(input("Choose (1) to create an account or; (2) to log into exisitng account: "))

if selected_option == 1:
    print(selected_option)

elif selected_option == 2:
    print(selected_option)

else:
    print("Invalid option. Try again.")