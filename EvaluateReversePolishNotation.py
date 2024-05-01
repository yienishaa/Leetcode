class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #In reverse Polish notation, the operators follow their operands. 
        #For example, to add 3 and 4 together, the expression is 3 4 + rather than 3 + 4. 
        #The conventional notation expression 3 − 4 + 5 becomes 3 4 − 5 + in reverse Polish notation
        #: 4 is first subtracted from 3, then 5 is added to it.

        res = 0
        stack = []
        for i in tokens:
            if i != "+" and i != "-" and i != "/" and i != "*":
                stack.append(int(i))
            else:
                a = stack[-1]
                stack.pop()
                b = stack[-1]
                stack.pop()

                if i is "+":
                    res = int(a) + int(b)
                elif i is "-":
                    res = int(b) - int(a)
                elif i is "*":
                    res = int(a)*int(b)
                else:
                    res = int(int(b)/int(a))
                
                stack.append(res)
        return stack[-1]
