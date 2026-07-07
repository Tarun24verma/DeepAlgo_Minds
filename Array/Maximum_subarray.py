import math
def max_subarray(a):
    # max_array=-math.inf
    # for i in range(len(a)):
    #     cur_sum=0
    #     for j in range(i,len(a)):
    #         cur_sum+=a[j]
    #         max_array=max(cur_sum,max_array)
    # return max_array
    max_till_now,cur_max=-math.inf,-math.inf
    for i in a:
        cur_max=max(i,cur_max+i)
        max_till_now=max(cur_max,max_till_now)
        
    return max_till_now
a=[-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(a))