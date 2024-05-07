class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        #monotonic decreasing problem or equal
        stack = [temperatures[0]]
        index_stack = [0]
        answer = [0]*len(temperatures)

        for i in range(1,len(temperatures)):
            if temperatures[i] > stack[-1]:
                for j in range(len(stack)-1,-1,-1):
                    if stack[j] < temperatures[i]:
                        stack.pop()
                        x = index_stack.pop()
                        answer[x] = i-x
            
            stack.append(temperatures[i])
            index_stack.append(i)

        return answer
