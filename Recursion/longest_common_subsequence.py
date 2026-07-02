s1 = "abcdefg"
s2 = "acdfg"
m = len(s1)
n = len(s2)
def lcs1(s1, s2, m, n):
    if m == 0 or n == 0:
        return 0
    if s1[m - 1] == s2[n - 1]:
        return 1 + lcs1(s1, s2, m - 1, n - 1)
    else:
        return max(lcs1(s1, s2, m, n - 1), lcs1(s1, s2, m - 1, n))
print(lcs1(s1, s2, m, n))