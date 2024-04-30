class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        count = 1
        mem_count = 0
        sorted_nums = sorted(nums)
        print(sorted_nums)

        for i in range(1,len(nums)):
            prev = sorted_nums[i-1]
            curr = sorted_nums[i]
            
            if (curr - prev) == 1 :
                count+=1
            else:
                if (curr - prev) > 1:
                    mem_count = max(count, mem_count)
                    count = 1
                

        mem_count = max(count, mem_count)

        return mem_count
