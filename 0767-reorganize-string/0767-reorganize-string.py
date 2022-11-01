class Solution:
    def reorganizeString(self, s: str) -> str:
        s_dict = collections.Counter(s)
        pq = [(-values, key) for key, values in s_dict.items()]
        heapq.heapify(pq)
        res = ""
        prev_freq, prev_ch = 0, ""
        while(pq):
            freq, ch = heapq.heappop(pq)
            res += ch
            freq += 1
            if prev_freq < 0:
                heapq.heappush(pq, (prev_freq, prev_ch))
            prev_freq, prev_ch = freq, ch
        # print(res)
        if len(res) != len(s):
            return ""
        return res        
        """s_len = len(s)
        s_dict = collections.Counter(s)
        
        ch_high = max(s_dict.values())
        res = ""
        toRemove = []
        while(s_dict):
            for ch, num in s_dict.items():
                if num > 0:
                    res += ch
                    s_dict[ch] -= 1
                else:
                    toRemove.append(ch)
            for ch in toRemove:
                del s_dict[ch]
            
            # print(len(s_dict)==1, list(s_dict.items())[0][1] > 1)
            # print(list(s_dict.items())[0][0], list(s_dict.items())[0][1])
            if len(s_dict)==1 and list(s_dict.items())[0][1] >= 1:
                return ""
        return res"""
                