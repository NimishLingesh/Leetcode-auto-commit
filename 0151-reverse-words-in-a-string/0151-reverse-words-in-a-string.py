class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        ret = ' '.join(s[::-1])
        return ret