class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkSet = set()
        for i in range(len(nums)):
            if nums[i] in checkSet:
                return True
            checkSet.add(nums[i])
        return False
