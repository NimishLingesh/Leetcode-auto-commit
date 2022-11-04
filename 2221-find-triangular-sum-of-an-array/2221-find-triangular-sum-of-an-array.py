class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        lst = []
        for i in range(len(nums)-1):
            lst.append((nums[i] + nums[i+1])%10)
        # print(lst)
        return self.triangularSum(lst)