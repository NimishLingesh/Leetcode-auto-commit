class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            l,r = nums[i],nums[i]
            for j in range(i, n):
                l = min(l, nums[j])
                r = max(r, nums[j])
                res += r - l
        return res
    
        # wrong answer
        '''def helper(nums, num):
            if len(nums) < 2:
                return nums[0], nums[0], 0
            sub_min, sub_mx, sub_diff = helper(nums[:-1], nums[-1])
            # print(sub_min, sub_mx)
            mn = min(sub_min, num)
            mx = max(sub_mx, num)
            print("sub_min", sub_min, "num", num)
            print("sub_mx", sub_mx, "num", num)
            print("-----")
            diff = mx - mn
            print(diff + sub_diff)
            return mn, mx, diff + sub_diff
        
        nums_len = len(nums)
        first = 0
        total = 0
        # for second in range(nums_len-1, first, -1):
        #     mn, mx, diff = helper(nums[first:second], nums[second])
        #     total += diff
            
        for first in range(nums_len):
            mn, mx, diff = helper(nums[first:nums_len-1], nums[nums_len-1])
            total += diff
        return total'''

        # TLE
        """res = 0
        nums_len = len(nums)
        for i_idx, i in enumerate(nums[:-1]):
            for j_idx in range(i_idx, nums_len):
                min_val = min(nums[i_idx: j_idx+1])
                max_val = max(nums[i_idx: j_idx+1])
                diff = max_val - min_val
                res += diff
        return res"""