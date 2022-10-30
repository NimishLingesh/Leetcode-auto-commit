class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        
        def isFeasible(threshold):
            total = 0
            sub_arrays = 1
            for num in nums:
                total += num
                if total > threshold:
                    sub_arrays += 1
                    total = num
                    if sub_arrays > k:
                        return False
            return True
        
        while left < right:
            mid = left + (right - left)//2
            if isFeasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
                