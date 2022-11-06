class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            s = "".join(sorted(s))
            return s
        else:
            visited = set([s])
            tmp = s
            first, tmp = tmp[0], tmp[1:]
            tmp = tmp + first
            while(tmp!=s):
                if tmp not in visited:
                    visited.add(tmp)
                    first, tmp = tmp[0], tmp[1:]
                    tmp = tmp + first
            print(visited)
            return min(visited)