# DP
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         rs = [amount+1] * (amount+1)
#         rs[0] = 0
#         for i in range(1, amount+1):
#             for c in coins:
#                 if i >= c:
#                     rs[i] = min(rs[i], rs[i-c] + 1)

#         # if rs[amount] == amount+1:
#         #     return -1
#         # return rs[amount]
        
# BFS
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        queue = [[0, 0]]
        visited = {0}
        step = 0
        for node, step in queue:
            for coin in coins:
                if node + coin in visited: continue
                if node + coin == amount: return step + 1
                elif node + coin < amount:
                    queue.append([node + coin, step + 1])
                    visited.add(node + coin)
        return -1