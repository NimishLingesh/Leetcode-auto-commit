class Solution:
    def uniqueLetterString(self, S: str) -> int:
        index = {c: [-1, -1] for c in ascii_uppercase}
        res = 0
        for i, c in enumerate(S):
            k, j = index[c]
            res += (i - j) * (j - k)
            index[c] = [j, i]
        for c in index:
            k, j = index[c]
            res += (len(S) - j) * (j - k)
        return res % (10**9 + 7)
    
        """self.res = 0
        l = len(s)
        for idx, ch in enumerate(s):
            # s_dict = defaultdict(lambda: 0)
            s_dict = {}
            total = l-idx
            sub = 0
            for i in range(idx, l):
                if s[i] not in s_dict:
                    s_dict[s[i]] = 1
                elif s_dict[s[i]] == 1:
                    s_dict[s[i]] += 1
                    sub += 1
                print(i-idx-sub+1)
                self.res += i-idx-sub+1
                # self.res += total-sub
                # self.countUniqueChars(s_dict)
        return self.res
                
    def countUniqueChars(self, s):
        val = s.values()
        sum_s = 0
        for v in val:
            if v == 1:
                self.res +=1"""
    
""" def uniqueLetterString(self, s: str) -> int:
        self.res = 0
        l = len(s)
        for idx, ch in enumerate(s):
            for i in range(idx, l+1):
                self.countUniqueChars(s[idx:i])
        return self.res
                
    def countUniqueChars(self, s):
        val = Counter(s).values()
        sum_s = 0
        for v in val:
            if v == 1:
                self.res +=1"""