
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii
import Crypto.Signature.pkcs1_15

# Generate 1024-bit RSA key pair (private + public key)
keyPair = RSA.generate(bits=1024)

# Get just the public key
justPubKey = keyPair.publickey()

# The good message
msg = b'hello'

# The tempered message
msg1 = b'tempered'

# Compute the hashes of both messages
hash = SHA256.new(msg)
hash1 = SHA256.new(msg1)

# Sign the hash
sig1 = Crypto.Signature.pkcs1_15.new(keyPair)
signature = sig1.sign(hash)

##################### On the arrival side #########################
# Note, we will have to take the decrypted message, hash it and then provide the
# hash and the signature to the
# verify function
verifier = Crypto.Signature.pkcs1_15.new(justPubKey)

# If the verification succeeds, nothing is returned. Otherwise a ValueError
# exception is raised
# Let's try this with the valid message
try:
    sig1.verify(hash, signature)
    print("The signature is valid!")
except ValueError:
    print("The signature is not valid!")

hash = hash1

# Now with the invalid message
try:
    sig1.verify(hash1, signature)
    print("The signature is valid!")
except ValueError:
    print("The signature is not valid!")
