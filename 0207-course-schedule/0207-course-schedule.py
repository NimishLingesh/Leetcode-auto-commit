class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """self.visited = set()
        prereq = defaultdict(list)
        for ele in prerequisites:
            prereq[ele[0]].append(ele[1])
        self.res = True

        
        def helper(course):
            if course not in prereq:
                # self.visited.add(course)
                return
            # elif any(x in self.visited for x in prereq[course]):
            #     self.res = False
            #     return 
            pre_c = prereq[course]
            
            # self.visited.add(course)
            for c in pre_c:
                helper(c)
                if self.res == False:
                    return
            prereq[course] = []

        for course in range(numCourses):
            # self.visited = {course}
            helper(course)
            if self.res == False:
                break
            
        return self.res"""
        
        prereq = defaultdict(list)
        for ele in prerequisites:
            prereq[ele[0]].append(ele[1])
        self.res = True
        
        visitedSet = set()
        def dfs(course):
            if course in visitedSet:
                return False
            if prereq[course] == []:
                return True
            
            visitedSet.add(course)
            for c in prereq[course]:
                ret = dfs(c)
                if ret == False:
                    return False
            visitedSet.remove(course)
            
            # setting the dict is empty is critical
            prereq[course] = []
            return True
        
        for course in range(numCourses):
            ret = dfs(course)
            if ret == False:
                return False
        return True
        
            