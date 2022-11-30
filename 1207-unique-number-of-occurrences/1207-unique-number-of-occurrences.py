class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_cnt = Counter(arr)
        occr = arr_cnt.values()
        return len(occr) == len(set(occr))