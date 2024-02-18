import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Server's IP address
SERVER_IP = "127.0.0.1"

# The server's port number and key
SERVER_PORT = 1235
KEY = input("Enter 16-byte key: ").encode('utf-8')

# The client's socket
cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Attempt to connect to the server
cliSock.connect((SERVER_IP, SERVER_PORT))

# Send the message to the server
msg = str(input("\nPlease enter a message to send to the server: "))

# print(msg
# Send the message to the server
# NOTE: the user input is of type string
# Sending data over the socket requires.
# First converting the string into bytes.
# encode() function achieves this.)

cipher = AES.new(KEY, AES.MODE_ECB)

# Convert msg into bytes
msgBytes = msg.encode('utf-8')

# Add padding
paddedMsg = pad(msgBytes, AES.block_size)

# Encrypt msg
encryptedMsg = cipher.encrypt(paddedMsg)
print("Encrypted: " + str(encryptedMsg))

# Send to server
cliSock.sendall(encryptedMsg)