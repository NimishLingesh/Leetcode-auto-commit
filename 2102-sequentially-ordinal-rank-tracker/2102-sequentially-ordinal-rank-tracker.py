import sortedcontainers

class SORTracker:
    def __init__(self):
        self.sortedList = sortedcontainers.SortedList()
        self.i = 0

    def add(self, name: str, score: int) -> None:
        self.sortedList.add([-score, name])

    def get(self) -> str:
        ans = self.sortedList[self.i][1]
        self.i += 1
        return ans
    
    # Need to use two queues - This solution is failing in the very first case
    """def __init__(self):
        self.query = -1
        self.q = []
        

    def add(self, name: str, score: int) -> None:
        heapq.heappush(self.q, (-score, name))

    def get(self) -> str:
        self.query += 1
        # return heapq.heappop(self.q)[1]
        # return self.q[self.query][1]
        tmp_dict = {}
        popped = heapq.heappop(self.q)
        if len(self.q)>1 and popped[0] == self.q[0][0]:
            for idx, i in enumerate(self.q):
                if i[0] == popped[0]:
                    tmp_dict[i[1]] = idx
                else:
                    break
            print("tmp_dict", tmp_dict)
            
            st = min(tmp_dict.keys())
            self.q.pop(int(tmp_dict[st]))
            heapq.heappush(self.q, popped)
            return st
        else:
            return popped[1]"""
        
        


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()