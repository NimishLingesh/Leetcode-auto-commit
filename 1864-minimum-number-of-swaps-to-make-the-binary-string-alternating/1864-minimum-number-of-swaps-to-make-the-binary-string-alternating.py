class Solution:
    def minSwaps(self, s: str) -> int:
        """ones = 0
        zeros = 0
        
        prev = None
        
        s_list = list(s)
        for idx, ch in enumerate(s_list):
            if prev == None:
                prev = ch
                continue
            if ch == '1':
                if ch == prev:
                    ones += 1
                    s_list[idx] = '0'
            elif ch == '0':
                if ch == prev:
                    zeros += 1
                    s_list[idx] = '1'
            prev = s_list[idx]
        # print(ones)
        # print(zeros)
        if ones != zeros:
            if abs(ones-zeros) == 1 and "1" in s_list and "0" in s_list and len(s_list)<4:
                return 1
            else:
                return -1
        else:
            return ones
            """
        
        ones = s.count("1")
        zeros = len(s) - ones
        if abs(ones-zeros) > 1:
            return -1
        
        def helper(s, c):
            total = 0
            for ch in s:
                if ch != c:
                    total +=1
                c = int(c)
                c ^= 1
                c = str(c)
            return total
        
        if ones > zeros:
            res = helper(s, "1")
        elif zeros > ones:
            res = helper(s, "0")
        else:
            res = min(helper(s, "1"), helper(s, "0"))
        return res//2