from Cryptodome.Signature import DSS
from Crypto.Hash import SHA256

# Create a new DSA key
key = DSS.generate(2048)
f = open("dsa_public_key.pem", "wb")
f.write(key.publickey().export_key())
f.close()

# Sign a message
message = b"Hello"
hash_obj = SHA256.new(message)
signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(hash_obj)

# Load the public key
f = open("dsa_public_key.pem", "rb")
hash_obj = SHA256.new(message)
pub_key = DSS.import_key(f.read())
verifier = DSS.new(pub_key, 'fips-186-3')

# Verify the authenticity of the message
try:
    verifier.verify(hash_obj, signature)
    print("The message is authentic.")
except ValueError:
    print("The message is not authentic.")
