
# Write a function, no_repeats(year_start, year_end), which takes a
# range of years and outputs those years which do not have any
# repeated digits.
#
# You should probably write a helper function, no_repeat?(year) which
# returns true/false if a single year doesn't have a repeat.
#1224 -141, 145-53, 1.5 hrs! 

#list(str(year)) #['1', '9', '6', '9'], 1969

year = 1970
def repeats_finder(year):
    # Alternative:
    # chars = list(str(year))
    # return len(set(chars)) == len(chars)
    year = list(str(year))
    for num in year:
        if year.count(num) > 1: # false == are repeats 1969
            return False
        
    return True # no repeats 1970
  
        
#print no_repeats_helper(1970) #true
#print no_repeats_helper(1971) #false
        
def no_repeats(year_start, year_end):
    years_no_repeated_digits = [] 
    for year in range(year_start, year_end + 1):
        if repeats_finder(year):
            years_no_repeated_digits.append(year)
    return years_no_repeated_digits
            
    
#print no_repeats(1988, 2005) #none
print no_repeats(1969, 1975) #1970?
print no_repeats(1923, 1960) #many!