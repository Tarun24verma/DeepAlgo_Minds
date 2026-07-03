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
# class Solution:
#     def removeUtil (self, s):
#         def dup(s):
#             resultant=[]
#             check=0
#             i = 0
#             while i < len(s):
#                 if i < len(s) - 1 and s[i] == s[i+1]:
#                     check += 1
#                     while i < len(s) - 1 and s[i] == s[i+1]:
#                         i += 1
#                 else:
#                     resultant.append(s[i])
#                 i += 1
#             if check == 0:
#                 return "".join(resultant)
#             return dup("".join(resultant))
#         a=dup(s)
#         if a:
#             return "".join(a)
#         else:
#             return '""'
result=""
i=0
s="geeksforgeek"
# while i<len(s):
#     if i < len(s) - 1 and s[i] == s[i+1]:
#         while i < len(s) - 1 and s[i] == s[i+1]:
#             i += 1
#     else:
#         result.append(s[i])
#     i += 1
# print("".join(result))
while i<len(s):
    a=s[i]
    while i<len(s) and s[i]==a:
        i+=1
    result += a
print(result)