from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        count = 0
        result = [0] * len(temperatures)
        indexes = []

     

        for i in range(len(temperatures)):
            
            if not stack:
                stack.append(temperatures[i])
                indexes.append(i)
            elif stack[-1] >= temperatures[i]:
                 stack.append(temperatures[i])
                 indexes.append(i)
            else:
                while stack and stack[-1]<temperatures[i]:
                    result[indexes[-1]] = i - indexes[-1]
                    stack.pop()
                    indexes.pop()
                
                stack.append(temperatures[i])
                indexes.append(i)
            
        
        return result

#temperatures = [73,74,75,71,69,72,76,73]
#temperatures = [30,40,50,60]
temperatures = [30,60,90]
tester = Solution()
result = tester.dailyTemperatures(temperatures)
print(result)
