class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = 0
        pos = 0
        neg = 0
        res = 0
        
        # very critical point: pos and neg should be updated at the same time, then write code in a single line
        for num in nums:
            if num > 0:
                pos = pos + 1
                # neg = 1 + neg if neg else 0
                if neg:
                    neg += 1
            elif num < 0:
                # neg = 1 + pos
                pos, neg = 1 + neg if neg else 0, 1 + pos
                # if neg:
                #     pos = 1 + neg
                # neg = 1 + pos
            else:
                pos = neg = 0
            ans = max(ans, pos)
        return ans