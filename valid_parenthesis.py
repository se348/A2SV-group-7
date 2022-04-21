class Solution:
    def isValid(self, s: str) -> bool:
        dictionary= {"(": ")","{": "}","[": "]"}
        stack_a =[]
        for i in s:
            if i in dictionary:
                stack_a.append(i)
            elif i in dictionary.values():
                if len(stack_a)==0:
                    return False
                if dictionary[stack_a[-1]] != i:
                    return False
                else:
                    stack_a.pop()
        if len(stack_a)==0:
            return True
s= Solution()
d =s.isValid("([)")
print(d)