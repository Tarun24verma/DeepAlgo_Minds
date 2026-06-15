class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pair={'(':')', '{':'}', '[':']'}
        for i in s:
            if i=='('or i=='{'or i=='[':
                stack.append(i)
            else:
                if not stack or pair[stack[-1]]!=i:
                    return False
                stack.pop()
        return len(stack)==0