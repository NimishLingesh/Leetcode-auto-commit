class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        char_set = []
        l = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.pop(0)
            char_set.append(s[r])
            res = max(res, len(char_set))
        return res
        
        """used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used[c] = i
        return max_length"""