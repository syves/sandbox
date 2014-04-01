# Write a method, ordered_vowel_words(str) that takes a string of
# lowercase words and 
#returns a string with just the words containing
# all their vowels (excluding "y") in alphabetical order. Vowels may
# be repeated (`"afoot"` is an ordered vowel word).
#
# You will probably want a helper method, ordered_vowel_word?(word)
# which returns true/false if a word's vowels are ordered.

#824 -10 10-130

import re

def is_ordered(word):
    vowels = re.sub(r'[^aeiou]',"", word.lower())#rid of non vowels
    #compare colwes to sorted voels
    return list(vowels) == sorted(vowels)        
    
print is_ordered("Shoes") 
print is_ordered("maybe")  

def ordered_vowels_words(string):
    words = string.lower().split()
    return " ".join([w for w in words if is_ordered(w)])
    #filter?
   
print ordered_vowels_words("Shoes in the boxes")

print "maybe she".split()
print list("maybe")
