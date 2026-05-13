class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''maxOnes = 0
        curr = 0
        for i in nums:
            if i == 0:
                maxOnes = max(maxOnes, curr)
                curr = 0
            else:
                curr += 1
        return max(maxOnes, curr)'''

        maxOnes = curr = 0
        for i in nums:
            curr = curr + 1 if i else 0
            maxOnes = max(maxOnes, curr)

        return maxOnes