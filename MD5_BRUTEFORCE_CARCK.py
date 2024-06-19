import hashlib
import itertools
import string
from tqdm import tqdm

total_characters = ""

letters = True
digits = True
punctuation = True

if letters == True:
    total_characters += string.ascii_letters
if digits == True:
    total_characters += string.digits
if punctuation == True:
    total_characters += string.punctuation

md5_hash = "098f6bcd4621d373cade4e832627b4f6"
min_length = 1
max_length = 8

for length in range(min_length, max_length + 1):
    total_combinations = len(total_characters) ** length
    for combination in tqdm(itertools.product(total_characters, repeat=length), total=total_combinations, desc=f"Length {length}"):
        word = ''.join(combination)
        
        if hashlib.md5(word.encode()).hexdigest() == md5_hash:
            print("Found it with word = " + word)
