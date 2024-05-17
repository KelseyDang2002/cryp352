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

Now if the user enters a wrong password or the account with the specifies username does not exist,
the login should be denied.
'''

import bcrypt
import pwinput

def create_account():
    username = input("Pick a username: ")
    password = pwinput.pwinput(prompt = "Pick a password: ")
    print("\nYou entered: ", username, " ", password)
    return username, password

def log_in():
    username = input("Enter existing username: ")
    password = pwinput.pwinput(prompt = "Enter the password: ")
    print("\nYou entered: ", username, " ", password)
    return username, password

def hash_password(password):
    password_in_bytes = bytes(password, 'utf-8')
    password_in_bytes = password.encode('utf-8')
    print("Password converted to bytes: ", type(password_in_bytes), password_in_bytes)
    salt = bcrypt.gensalt()
    print("\nSalt: ", salt)
    hashed_password = bcrypt.hashpw(password_in_bytes, salt)
    print("Hashed password: ", hashed_password)
    return hashed_password

def store_in_db(username, hashed_password_in_bytes):
    hashed_password = hashed_password_in_bytes.decode('utf-8')
    account = username + " " + hashed_password + "\n"
    print("\nAppend ", account, "to db.txt")
    print(type(account))
    file_append = open("db.txt", "a")
    file_append.write(account)
    file_append.close()
    print("\nAccount successfully created! Run the program again and try to log in.")

def check_if_in_db(username, password):
    account_dict = {}

    print("\nUsername: ", username)
    print("Password: ", password)

    password_in_bytes = bytes(password, 'utf-8')
    password_in_bytes = password.encode('utf-8')
    
    file_read = open("db.txt", "r")

    for accounts in file_read:
        user, hashed_password = accounts.strip().split(" ")
        account_dict[user] = hashed_password

    file_read.close()

    print("\n", account_dict)

    for user, hashed_password in account_dict.items():
        if username == user:
            print(user, " ", hashed_password)
            hashed_password_in_bytes = bytes(hashed_password, 'utf-8')
            hashed_password_in_bytes = hashed_password.encode('utf-8')
            if bcrypt.checkpw(password_in_bytes, hashed_password_in_bytes):
                print("\nPasswords match! Successfully logged in.")
            else:
                print("\nIncorrect password. Run the program again.")
            break

# prompt user with options
selected_option = int(input("Choose (1) to create an account or; (2) to log into existing account: "))

if selected_option == 1:
    username, password = create_account()
    hashed_password_in_bytes = hash_password(password)
    store_in_db(username, hashed_password_in_bytes)

elif selected_option == 2:
    username, password = log_in()
    check_if_in_db(username, password)

else:
    print("Invalid option. Try again.")