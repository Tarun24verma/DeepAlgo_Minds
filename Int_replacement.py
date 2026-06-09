class Solution:
    def integerReplacement(self, n: int) -> int:
        if n==1:
            return 0
        def even_treat(n):
            n=n//2
            return n
        def odd_treat(n):
            if (n&3)==3 and n!=3:
                n+=1
            else:
                n-=1
            return n
        count=0
        while n>1:
            if n%2==0:
                n=even_treat(n)
            else:
                n=odd_treat(n)
            count+=1
        return count