class Solution:
    def frequencySort(self, s: str) -> str:
        s_counter = Counter(s)
        hp = []
        for key, val in s_counter.items():
            heappush(hp, (-val, key))
        ret = ""
        while(len(hp)):
            num, ele = hp.pop(0)
            heapq.heapify(hp)
            for i in range(-num):
                ret += ele
        return ret