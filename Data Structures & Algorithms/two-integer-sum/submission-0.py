class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''output = []
        for i in range(len(nums)):
            j = (target-nums[i])
            if j in nums:
                output.extend([i,nums.index(j)])
                return output

#two pointer method
        A = []
        for i, num in enumerate(nums):
            A.append([i, num])
        A.sort()
        x, y = 0, len(nums)-1
        while x < y:
            if A[x][1] + A[y][1] == target:
                return [A[x][0], A[y][0]]
            elif A[x][1] + A[y][1] < target:
                x += 1
            elif A[x][1] + A[y][1] > target:
                y -= 1'''

#hash map method (efficient)
        inc = {}

        for i, n in enumerate(nums):
            inc[n] = i

        for j,m in enumerate(nums):
            diff = target - m

            if diff in inc and inc[diff] != j:
                return [j,inc[diff]]

