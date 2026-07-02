N=100
p=2
# """ways to get N with sum of digits which are n**p whare n is natural number."""
# p=[1,2,3,4,5,6,7,8,9,10]
# a=[i**3 for i in p if i**3<=N]
# def find_sum_of_all_possible_subsets_of_array(arr,start,end,sum):
#     if start > end:
#         if sum==100:
#             print(arr)
#         return
#     find_sum_of_all_possible_subsets_of_array(arr,start + 1, end, sum + arr[start])
#     find_sum_of_all_possible_subsets_of_array(arr,start + 1, end, sum)

# find_sum_of_all_possible_subsets_of_array(a,0,(len(a)-1),0)
def count_ways(N,p,num):
    value=N-pow(num,p)
    if value==0:
        return 1
    if value<0:
        return 0
    return count_ways(value,p,num+1)+ count_ways(N,p,num+1)