class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        res = [0] * len(tasks)
        available = []
        for i in range(len(servers)):
            available.append([servers[i], i])
        heapq.heapify(available)
        unavailable = []
        t = 0
        for i in range(len(tasks)):
            t = max(i, t)
            
            if len(available) == 0:
                t = unavailable[0][0]
            while unavailable and unavailable[0][0] <= t:
                free_time, weight, index = heapq.heappop(unavailable)
                heapq.heappush(available, [weight, index])
            
            server_weight, index = heapq.heappop(available)
            res[i] = index
            heapq.heappush(unavailable, [t+tasks[i], server_weight, index])
        return res
            
            