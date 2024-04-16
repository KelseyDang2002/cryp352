#!/usr/bin/python

import bcrypt

# The password to hash
# password = b'hello'

# Generate the salt value
salt = bcrypt.gensalt()

# print("The salt is ", salt)

enteredpass = input("Please enter a password: ")

# Hash the password
# hashed = bcrypt.hashpw(password, salt)
hashed = b'$2b$12$TUChp.a11tYo20sF8xlL9e30PeqcuWQOQ5KXbMSmzp/b/Vf3/o8qy'

print("The hash is: ", hashed)

# Verify if the password matches
if bcrypt.checkpw(enteredpass.encode(), hashed):
    print("Passwords match!")
else:
    print("Passwords DO NOT match!")
