

lst = [37, 996, 28, 10]

def times_3(num):
    return num * 3
        
def times_2(num):
    return num * 2


def make_multiplier(n):
    lambda m: m * n
    
times_3 = make_multiplier(3)
times_2 = make_multiplier(2)

def product(a, b):
    return a * b

import functools

times_3 = functools.partial(product, 3)
times_2 = functools.partial(product, 2)

        
print map(times_2, lst)

print [nums * 2 for nums in lst]

#:)
