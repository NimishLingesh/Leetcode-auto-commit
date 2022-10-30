# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first = 0
        second = n
        
        while first<second:
            mid = first + (second - first)//2
            if isBadVersion(mid):
                second = mid
            else:
                first = mid + 1
        return first