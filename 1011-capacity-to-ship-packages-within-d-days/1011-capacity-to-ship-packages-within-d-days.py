class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def isFeasible(load):
            total = 0
            # important to set the number of days as 1 as you are calculating the weight already in a day
            no_of_days = 1
            for weight in weights:
                total += weight
                if total > load:
                    no_of_days += 1
                    total = weight
                    if no_of_days > days:
                        return False
            return True
            
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = left + (right - left)//2
            if isFeasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
        