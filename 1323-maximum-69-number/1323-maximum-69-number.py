class Solution:
    def maximum69Number (self, num: int) -> int:
        s_num = str(num)
        for idx, ch in enumerate(list(s_num)):
            if ch == "6":
                s_num = s_num[:idx] + "9" + s_num[idx+1:]
                return eval(s_num)
        return num