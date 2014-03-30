#good work! 1105 1123- 1123-1135 enumerate, 1135-51 searching 1206 1 hr!!!

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
       
print nearest_larger([2,5,6,7,1,7], 2) #7
print nearest_larger([2,5,8,7,1,7], 2) #nil
print nearest_larger([2,5,7,7,1,7], 2) #7

