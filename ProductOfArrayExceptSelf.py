from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #method 2 with improved space complexity
        result = [1] * len(nums)
        
        
        #1st pass
        for i in range(1,len(nums)):
            result[i] = result[i-1] * nums[i-1]

        post = 1
        #2nd pass
        for i in range((len(nums)-1),-1,-1):
           result[i] = post * result[i]
           post = post * nums[i]



        return result
    
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        #method 1 with improved space complexity
        result = [1] * len(nums)
        prefix = [1] * (len(nums)+1) #| 1| 1| 2|6|24|
        suffix = [1] * (len(nums)+1) #|24|24|12|4| 1|
        
        #1st pass
        #   |1 |2 |3 |4 | - nums
        #|1 |1 |1 |1 |1 | - prefix
        #|1 |1 |2 |6 |24|
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i] 

        #2nd pass
        #|1 |2 |3 |4 | - nums
        #|1 |1 |1 |1 |1 | - suffix
        #|24|24|12|4 |1 |
        for i in range((len(nums)-1),-1,-1):
           suffix[i] = suffix[i+1] * nums[i]

        for i in range(0,len(nums)):
           result[i] = prefix[i-1] * suffix[i+1]


        return result
    
tester = Solution()
nums = [1,2,3,4]
result = tester.productExceptSelf2(nums)
print(result)