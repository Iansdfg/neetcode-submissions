# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            level = []
            for i in range(len(queue)):
                next_node = queue.popleft()
                # print(next_node.val)
                level.append(next_node.val)
                if next_node.left:
                    queue.append(next_node.left)
                if next_node.right:
                    queue.append(next_node.right)
            res.append(level)
        return res 

        