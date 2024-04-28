class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        numset = set()
        result = False

        for i in nums:
            if i in numset:
                result = True
                break
            numset.add(i)
        
        return result

testInst = Solution()
nums1 = [1,1,1,3,3,4,3,2,4,2]
x = testInst.containsDuplicate(nums1)
print(x)