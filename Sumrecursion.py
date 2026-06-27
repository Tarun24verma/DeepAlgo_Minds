def sum_array(arr):
    
    return arr[0]+sum_array()
a=[1,2,3,4,5]
print(sum_array(a))