class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        idx_track = []
        s_list = list(s)
        
        ret = ''
        for idx, ch in enumerate(s_list):
            if ch.isalnum():
                ret += ch
        # for idx in idx_track:
        #     s = s[:idx] + s[idx+1:]
        print(ret)
        return ret == ret[::-1]