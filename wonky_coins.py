from __future__ import division
import operator

# Catsylvanian money is a strange thing: they have a coin for every
# denomination (including zero!). A wonky change machine in
# Catsylvania takes any coin of value N and returns 3 new coins,
# valued at N/2, N/3 and N/4 (rounding down).
#
# Write a method wonky_coins(n) that returns the number of coins you
# are left with if you take all non-zero coins and keep feeding them
# back into the machine until you are left with only zero-value coins.

#20 mins, 20, 20

def wonky_coins(num):
    zeros = 0
    for coin in (num // 2, num // 3, num // 4):
        zeros += 1 if coin == 0 else wonky_coins(coin)
    return zeros
    
assert wonky_coins(5) == 11