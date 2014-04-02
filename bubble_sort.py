import dis
# Write a function bubble_sort(arr) which will sort an array of
# integers using the "bubble sort"
# methodology. (http://en.wikipedia.org/wiki/Bubble_sort) 

def bubble_sort(arr):
    a = 0
    b = a + 1
    for num in arr: 
        if arr[a] > arr[b]:
            arr[a], arr[b] = arr[b], arr[a]
            a = + 1
        elif arr[a] < arr[b]:            
            a = a + 1
            b = b + 1
        else: #if arr[a] == arr[b]:
            a = a + 1
            b = b + 1      
        
    return arr
print "input array", [3, 22, 5, 22, 67, 32]
print "bubble sorted array", bubble_sort([3, 22, 5, 22,  67, 32]) 


        
        
        
