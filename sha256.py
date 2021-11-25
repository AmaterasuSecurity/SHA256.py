from pwn import *
import sys
import hashlib

ciphertext = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8" # password hash to crack
wordlist = "//usr//share//wordlists/rockyou.txt"

# This outputs hash w/ open filepath
with open(wordlist,encoding='latin-1') as f:
    for line in f: # repeating for each line in wordlist
        pass
        line = line.strip() # remove line break from each line 
        linehash = hashlib.sha256(line.encode()).hexdigest() # computing hash from line plaintext and saving to linehash
        
        if linehash == ciphertext:
            print("WE GOT EM")
            print(f'{linehash} --> {line}')

f.close()