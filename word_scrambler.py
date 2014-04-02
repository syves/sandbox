import itertools
# Write a function word_unscrambler that takes two inputs: a scrambled
# word and a dictionary of real words.  Your program must then output
# all words that our scrambled word can unscramble to.
#
# Hint: To see if a string s1 is an anagram of s2, split both
# strings into arrays of letters. Sort the two arrays. If they are
# equal, then they are anagrams.
#

text = "Your program must then output all words that our scrambled word can unscramble to must"

def make_dict(text):
    d = {}
    for word in text.split():
        d[word] = word
    return d
print make_dict(text)

d = {'then': 'then', 'all': 'all', 'word': 'word', 'unscramble': 'unscramble', 'that': 'that', 'to': 'to', 'scrambled': 'scrambled', 'program': 'program', 'can': 'can', 'words': 'words', 'our': 'our', 'output': 'output', 'Your': 'Your', 'must': 'must', 'sword': 'sword'}
#no duplicates,
#no aplh order

def word_unscrambler(scram_word, d):
    unscram_words = []
    scrambles = list(itertools.permutations(scram_word, len(scram_word)))
    for key in d:
        if sorted(d[key]) == sorted(scram_word):
            unscram_words.append(d[key])
    return unscram_words
    #how do I know if something is a real word? it must be in {}
    #should I get a real dictonary? code should be the same
    #use safe get()
    
print word_unscrambler("sword", d)
    

 


