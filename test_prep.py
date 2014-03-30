'''
Estimated time: 1hr

Write a method that takes an array of integers and returns an array with the array elements multiplied by two.

Write a method that finds the median of a given array of integers. If the array has an odd number of integers, return the middle item from the sorted array. If the array has an even number of integers, return the average of the middle two items from the sorted array.

Create a method that takes in an Array of Strings and uses inject to return the concatenation of the strings.
'''

#854-922 for wrong set up. dismiss was trying to solve wrong problem

'''
_list = [1, 3, 5, 8, 1]
def summ(array):
    sum_ = 0
    for num in array:
        sum_ += num
    return sum_
print summ(_list)
       
def times_two(_list):
   # _list = [1, 3, 5, 8]
    #for nums in list_:
    return [num * 2 for num in _list]
    
print times_two([1, 3, 5, 8])


#10:20-11:37 1. hr 26 minutes !
def median(array):
    idx = len(array)/2 
    #if even do: return middle item
    if len(array) % 2 == 0:
        return sum(sorted(array)[idx - 1: idx + 1]) / 2.0
    else: #odd
        return sorted(array)[idx]
        
print median([2,5,6,7,1,7])# [1, 2, 5, 6, 7, 7], len 6, 5+6 /2 =                        
print median([2,5,6,7,1])# [1, 2, 5, 6, 7], len 5, min num = 5

#1143-1146, 1208-1210 5 minutes :)
def cat(array):
    for items in array:
        if type(str):
            return "".join(array)
 '''            
#good work! 1105 1123- 1123-1135 enumerate, 1135-51 searching 

# Write a function, `nearest_larger(arr, i)` which takes an array and an
# index.  The function should return another index, `j`: this should
# satisfy:
#
# (a) `arr[i] < arr[j]`, AND
# (b) there is no `j2` closer to `i` than `j` where `arr[i] < arr[j]`.
#
# In case of ties (see example below), choose the earliest (left-most)
# of the two indices. If no number in `arr` is larger than `arr[i]`,
# return `nil`.
'''
arr = sorted([2,5,6,7,1,7])
print sorted([2,5,6,7,1,7])
print [(i, j) for i,j in enumerate(sorted(arr))]
'''
    
def nearest_larger(arr, i):
    j = i + 1
    if arr[i] < arr[j]:
        if arr[j] > arr[j + 1]:
            
            return arr[j]
        else:
            return arr[j + 1]
            
    elif arr[i] == arr[j]:
        return  arr[i]
    else:
        return 'nil'
       
print nearest_larger([2,5,6,7,1,7], 2)
print nearest_larger([2,5,8,7,1,7], 2)
print nearest_larger([2,5,7,7,1,7], 2)





