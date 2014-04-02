
from collections import Counter
# Write a function, `letter_count(str)` that takes a string and
# returns a hash mapping each letter to its frequency. Do not include
# spaces.
#

def letter_counts(text):
    #for char in text, add char is new key, 
    #incremet value for occurance
    return Counter(text)

print letter_counts("cata")

#or return a {}

def letter_counts(text):
    #for char in text, add char is new key, 
    #incremet value for occurance
    d = {}
    for char in text:
        d[char] = d.get(char, 0) + 1
        
    return d

print letter_counts("cata")


