### To install the pycryptodome library ####
# sudo apt install python3-pip
# sudo pip3 install pycryptodomex

from Cryptodome.Cipher import AES

######### BASIC ENCRYPTION ###########

# The key (must be 16 bytes = 128 bit)
key = b'Sixteen byte key' # b = raw byte

# Set up the AES encryption class
# encCipher = AES.new(key, AES.MODE_ECB) # new used to create instance

# AES requires plain/cipher text blocks to be 16 bytes
# cipherText = encCipher.encrypt(b'hello12345678s0d1111111111111111') # 2 blocks worth

# print("Cipher text: ", cipherText)

# encFile = open("encrypted.enc", "wb")
# encFile.write(cipherText)
# encFile.close()

cipherFile = open("encrypted.enc", "rb")
cipherText = cipherFile.read()
cipherFile.close()

########### BASIC DECRYPTION ##############

# Set up the AES encryption class
decCipher = AES.new(key, AES.MODE_ECB)

# AES requires plain/cipher text blocks to be 16 bytes
plainText = decCipher.decrypt(cipherText)

print("Decrypted text: ", plainText)

decFile = open("plain.dec", "wb")
decFile.write(plainText)
decFile.close()
