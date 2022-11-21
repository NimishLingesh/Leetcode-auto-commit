class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        self.nearest = -1
        q = [entrance]
        direction = [(0,1), (1,0), (-1, 0), (0, -1)]
        visited = set()
        step_track = 0
        def helper(position, steps):
            i, j = position[0], position[1]
            if i < 0 or i >= len(maze) or j < 0 or j >= len(maze[0]):
                if self.nearest <= 0:
                    self.nearest = steps-1
                else:
                    self.nearest = min(steps-1, self.nearest)
                return
            elif maze[i][j] == "+":
                return
            # if (i == 0 or j == 0 or i==len(maze)-1 or j == len(maze[0])-1) and maze[i][j] == ".":
            #     if self.nearest == -1:
            #         self.nearest = steps
            #     else:
            #         self.nearest = min(steps, self.nearest)
            #     return
            if tuple(position) not in visited and maze[i][j] == ".":
                # q.append(tuple(position))
                maze[position[0]][position[1]] = steps
                # if (i == 0 or j == 0 or i==len(maze)-1 or j == len(maze[0])-1):
                #     if self.nearest == -1:
                #         self.nearest = steps
                #     else:
                #         self.nearest = min(steps, self.nearest)
                #     return
                # else:
                q.append(tuple(position))
            
        while(q):
            # print("q -> ", q)
            step_track += 1
            for _ in range(len(q)):
                q_point = q.pop(0)
                i = q_point[0]
                j = q_point[1]
                if tuple(q_point) not in visited and maze[i][j] != "+":
                    visited.add(tuple(q_point))
                    for mov in direction:
                        helper([q_point[0]+mov[0], q_point[1]+mov[1]], step_track)
        print(maze)
        # print(visited)
        if self.nearest == 0:
            return -1
        else:
            return self.nearest