#!/home/rhyme/penv/bin/python3

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


import sys, os

if (len(sys.argv)) != 2:
    print ('Usage: ./encrypt.py original_filename')
    exit(-1)

