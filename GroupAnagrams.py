from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        bucket = defaultdict(list) #hashmap to hold pattern:[words]

        for words in strs:
            arr = [0] * 26 #26 spaceholders to count the number of each alphabet in the word
            for c in words:
                arr[ord(c) - ord("a")]+=1 #here we update alphabet array with total number of letters in the word
            
            bucket[tuple(arr)].append(words) #append the word to the bucket with the key = arr array used a key. Note array type cant be used as a key
            print(bucket)
            

        return bucket.values()

strs = ["eat","tea","tan","ate","nat","bat"]
tester = Solution()
result = tester.groupAnagrams(strs)
print(result)