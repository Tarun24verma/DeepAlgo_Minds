# a=[1,2]
# def sums(a,ex):
#     if ex==len(a)-1:
#         return a
#     ex+=1
#     sums(a,ex)
#     a[ex]=0
#     print(sum(sums(a,ex)))
# sums(a,ex=0)
def find_sum_of_all_possible_subsets_of_array(arr,start,end,sum):
    if start > end:
        print(sum)
        return
    find_sum_of_all_possible_subsets_of_array(arr,start + 1, end, sum + arr[start])
    find_sum_of_all_possible_subsets_of_array(arr,start + 1, end, sum)

find_sum_of_all_possible_subsets_of_array([1,2,3],0,2,0)