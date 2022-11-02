# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        conn = collections.defaultdict(list)
        def connect(parent, child):
            # both parent and child are not empty
            if parent and child:
                # building an undirected graph representation, assign the
                # child value for the parent as the key and vice versa
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            # in-order traversal
            if child.left: connect(child, child.left)
            if child.right: connect(child, child.right)
        # the initial parent node of the root is None
        connect(None, root)
        # start the breadth-first search from the target, hence the starting level is 0
        bfs = [target.val]
        seen = set(bfs)
        # all nodes at (k-1)th level must also be K steps away from the target node
        for i in range(K):
            # expand the list comprehension to strip away the complexity
            new_level = []
            for q_node_val in bfs:
                for connected_node_val in conn[q_node_val]:
                    if connected_node_val not in seen:
                        new_level.append(connected_node_val)
            bfs = new_level
            # add all the values in bfs into seen
            seen |= set(bfs)
        return bfs

        
        # level order traveresed but got stuck to traverse back and get the kth node
        """target_level = None
        q = [root]
        tree_dict = {}
        tree_dict[0] = [root.val]
        level = 0
        while(q):
            inner_q = []
            inner_q_val = []
            level +=1
            for i in range(len(q)):
                node = q.pop(0)
                if node.val == target.val:
                    target_level = level - 1
                if node.left:
                    inner_q.append(node.left)
                    inner_q_val.append(node.left.val)
                if node.right:
                    inner_q.append(node.right)
                    inner_q_val.append(node.right.val)
            tree_dict[level] = inner_q_val
            q.extend(inner_q)
            
            
        res = []
        next_level = target_level + k
        if next_level < len(tree_dict):
            res.extend(tree_dict[next_level])
        lower_level = target_level - k
        if lower_level < 0:
            
        return res"""