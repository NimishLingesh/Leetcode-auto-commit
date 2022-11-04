class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if 0 in nums:
            return len(set(nums))-1
        else:
            return len(set(nums))
        
        """count = 0
        while(0 in nums):
            nums.remove(0)
        while(len(nums)>0):
            count += 1
            lst = []
            m = min(nums)
            for idx, num in enumerate(nums):
                nums[idx] -= m
                if nums[idx] <= 0:
                    lst.insert(0, idx)
            for index in lst:
                nums.pop(index)
        return count"""