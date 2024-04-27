# Assignment 3 Question 7

'''
Requirements:

1. Prompt the user to enter two options (1) create an account or
login into the existing account

2. If the user chooses option (1) they are prompted with to select a username and password.
The program will then check file called db.txt that has the following format:

    each line consists of the:
    - username
    - space separator
    - salted hashed password (computed using the bcrypt library)

associated with the user.

3. If the user has a registered account in db.txt and enters a valid password 
(that is properly matched against the salted hash), they can attempt to login 
into their account by choosing option (2) at the intial prompt.

Now if the user enters a wronf password or the account with the specifies username does not exist,
the login should be denied.
'''

import bcrypt
import pwinput

# prompt user with options

selected_option = int(input("Choose (1) to create an account or; (2) to log into existing account: "))

if selected_option == 1:
    print(selected_option)

elif selected_option == 2:
    print(selected_option)

else:
    print("Invalid option. Try again.")