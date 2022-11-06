class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for ele in intervals:
            if len(res) == 0:
                res.append(ele)
                continue
            if ele[0] <= res[-1][1]:
                last_res = res.pop(-1)
                new_ele = [last_res[0], max(ele[1], last_res[1])]
                res.append(new_ele)
            else:
                res.append(ele)
        return res
                