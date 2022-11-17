class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums) - 1
        ret = []
        for idx, num in enumerate(nums[:-1]):
            l = idx+1
            r = n
            # local_sum = num + nums[l] + nums[r]
            while(l<r):
                local_sum = num + nums[l] + nums[r]
                if local_sum == 0:
                    lst = sorted([num, nums[l], nums[r]])
                    if lst not in ret:
                        ret.append(lst)
                    # break
                    l += 1
                if local_sum < 0:
                    l += 1
                elif local_sum:
                    r -= 1
        return ret