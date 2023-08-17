#!/opt/homebrew/bin/python3
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


import sys, os

if (len(sys.argv)) != 2:
    print ('Usage: ./capstone.py news_alert')
    exit(-1)

# the first command line argument is the news alert data.
# Use the given code to encode the data into bytes:
org_alert = sys.argv[1].encode()

# Read the public key from the file into a variable
# using the PUB_PEMK Environment Variable as the filename.

# encrypt the data



# Read the private key from the file into a variable
# using the PEMK Environment Variable as the filename.

# replace the following line of code and decrypt 
# the encrypted alert using the private key and assign 
# the decrpted data to the variable decrypted.


# print the decrypted alert (given below).
# print(decrypted.decode())


