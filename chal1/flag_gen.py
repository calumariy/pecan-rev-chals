from hashlib import sha256
import random

FLAG = "REDACTED"
encoder = 3

for i in range(len(FLAG)):
    current = ord(FLAG[i])
    
    current = current * encoder

    encoder += 1

    print(chr(current), end = "")
