class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        
        max_water = 0
        while(l<r):
            # h = min(height[l], height[r])
            if height[l] < height[r]:
                h = height[l]
                l += 1
            else:
                h = height[r]
                r -= 1
            w = r - l + 1
            capacity = h*w
            if capacity > max_water:
                max_water = capacity
        return max_water