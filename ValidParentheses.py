class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i is "(" or i is "[" or i is "{":
                stack.append(i)
            elif (i is ")" or i is "]" or i is "}") and not stack:
                return False
            elif (i is ")") and (stack[-1] != "("):
                return False
            elif (i is "]") and (stack[-1] != "["):
                return False
            elif (i is "}") and (stack[-1] != "{"):
                return False
            else:
                stack.pop()

        
        if stack:
            return False
        else:
            return True
