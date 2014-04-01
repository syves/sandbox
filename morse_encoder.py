import re

# Build a function, morse_encode(str) that takes in a string (no
# numbers or punctuation) and outputs the morse code for it. See
# http://en.wikipedia.org/wiki/Morse_code. Put two spaces between
# words and one space between letters.
#
# You'll have to type in morse code: I'd use a hash to map letters to
# codes. Don't worry about numbers.
#
# I wrote a helper method morse_encode_word(word) that handled a
# single word.

#20
import re

morse_dict = {
    "a": ". ---",
    "b": "--- . . .",
    "c": "--- . --- .",
    "d": "--- . .",
    "e": ".",
    "f": ". . --- .",
    "g": "--- --- .",
    "h": ". . . .",
    "i": ". .",
    "j": ". --- --- ---",
    "k": "--- . ---",
    "l": ". --- . .",
    "m": "--- ---",
    "n": "--- .",
    "o": "--- --- ---",
    "p": ". --- --- .",
    "q": "--- --- . ---",
    "r": ". --- .",
    "s": ". . .",
    "t": "---",
    "u": ". . ---",
    "v": ". . ---",
    "w": ". --- ---",
    "x": "--- . . ---",
    "y": "--- . --- ---",
    "z": "--- --- . ."
}

def make_morse_word(word):
    #clean_word = re.sub(r'[^a-z]',"", word)
    #join letters with one space
    return " ".join([morse_dict[c] for c in word if c in morse_dict])  
    #
      
print make_morse_word("888susanaa")

def morse_encoder(text):
#breaks strings into words
    return "  ".join(map( make_morse_word, text.split()))
             
print morse_encoder("have a great day")



    
    



