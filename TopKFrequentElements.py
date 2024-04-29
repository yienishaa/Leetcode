from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==1:
            return [k]
        
        bucket = {} #empty dictionary
        
        for i in nums:
            if i in bucket:
                bucket[i] = bucket.get(i) + 1
            else:
                bucket[i] = 1

        frequencies = sorted(bucket, key=bucket.get, reverse=True) #sorts the dictionary values in decending order

           
        return frequencies[:k]


tester = Solution()
nums = [1,1,1,2,2,3,3,3,3,3]
k = 2
result = tester.topKFrequent(nums,k)
print(result)
