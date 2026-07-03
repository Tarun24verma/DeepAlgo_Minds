# s="geeksforgeek"
# def dup(s):
#     resultant=[]
#     check=0
#     i = 0
#     while i < len(s):
#         if i < len(s) - 1 and s[i] == s[i+1]:
#             check += 1
#             while i < len(s) - 1 and s[i] == s[i+1]:
#                 i += 1
#         else:
#             resultant.append(s[i])
#         i += 1
#     if check == 0:
#         return "".join(resultant)
#     return dup("".join(resultant))

# a = dup(s)
# print(f'"{a}"' if a else '""')
class Solution:
    def removeUtil (self, s):
        def dup(s):
            resultant=[]
            check=0
            i = 0
            while i < len(s):
                if i < len(s) - 1 and s[i] == s[i+1]:
                    check += 1
                    while i < len(s) - 1 and s[i] == s[i+1]:
                        i += 1
                else:
                    resultant.append(s[i])
                i += 1
            if check == 0:
                return "".join(resultant)
            return dup("".join(resultant))
        a=dup(s)
        if a:
            return "".join(a)
        else:
            return '""'