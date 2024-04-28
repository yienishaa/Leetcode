class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ss = list(s)
        tt = list(t)

        ss.sort()
        tt.sort()

        return ss==tt

testInst = Solution()
s = "anagram"
t = "nagaram"
x = testInst.isAnagram(s,t)
print(x)