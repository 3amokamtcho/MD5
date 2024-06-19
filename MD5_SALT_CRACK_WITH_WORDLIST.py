import hashlib
import itertools
import string
from tqdm import tqdm

md5_hash = "89decd9231f11dee70b3911ea0b7fcbc"
md5_hashed_word = "test"

wordlist_path = "test.txt"

def load_wordlist(file_path):
    with open(file_path, 'r',encoding='utf-8', errors='ignore') as file:
        words = [line.strip() for line in file]
    return words
    
wordlist = load_wordlist(wordlist_path)
print("total of loaded words = " + str(len(wordlist)))

for x in tqdm(wordlist,"Processing HASH"):
    data_with_salt_left = x + md5_hashed_word
    data_with_salt_right = md5_hashed_word + x
    data_with_salt_center = x + md5_hashed_word + x
    
    if hashlib.md5(data_with_salt_left.encode()).hexdigest() == md5_hash:
        print(x  + " is the salt hash " + hashlib.md5(data_with_salt_left.encode()).hexdigest())
        print("full salt with data is = " + data_with_salt_left)
    elif hashlib.md5(data_with_salt_right.encode()).hexdigest() == md5_hash:
        print(x  + " is the salt hash " + hashlib.md5(data_with_salt_right.encode()).hexdigest())
        print("full salt with data is = " + data_with_salt_right)
    elif hashlib.md5(data_with_salt_center.encode()).hexdigest() == md5_hash:
        print(x  + " is the salt hash " + hashlib.md5(data_with_salt_center.encode()).hexdigest())
        print("full salt with data is = " + data_with_salt_center)

print("Finished HASH")
    
