import hashlib
import itertools
import string
from tqdm import tqdm

total_characters = ""

letters = True
digits = True
punctuation = True

if letters == False:
    total_characters += string.ascii_letters
if digits == False:
    total_characters += string.digits
if punctuation == True:
    total_characters += string.punctuation

md5_hash = "17f6752f269bb10d6346298e47592953"
md5_hashed_word = "kamtcho"
min_length = 1
max_length = 8

for length in range(min_length, max_length + 1):
    total_combinations = len(total_characters) ** length
    for combination in tqdm(itertools.product(total_characters, repeat=length), total=total_combinations, desc=f"Length {length}"):
        word = ''.join(combination)
        data_with_salt_left = word + md5_hashed_word
        data_with_salt_right = md5_hashed_word + word
        data_with_salt_center = word + md5_hashed_word + word
        
        if hashlib.md5(data_with_salt_left.encode()).hexdigest() == md5_hash:
            print("Found it with full word = " + data_with_salt_left)
        elif hashlib.md5(data_with_salt_right.encode()).hexdigest() == md5_hash:
            print("Found it with full word = " + data_with_salt_right)
        elif hashlib.md5(data_with_salt_center.encode()).hexdigest() == md5_hash:
            print("Found it with full word = " + data_with_salt_center)

