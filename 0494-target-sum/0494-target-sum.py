class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp = [0 for _ in range(len(nums[0])) for j in range(len(nums))
        dp = {}
        def backTrack(i, total):
            if i == len(nums):
                if target == total:
                    return 1
                else:
                    return 0
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = (backTrack(i+1, total + nums[i]) + backTrack(i+1, total - nums[i]))
            return dp[(i, total)]
        return backTrack(0,0)
             