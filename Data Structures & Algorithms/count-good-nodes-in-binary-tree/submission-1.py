# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    good_cnt = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, float('-inf'))
        return self.good_cnt

    def dfs(self, node, max_val):
        if node.val >= max_val:
            self.good_cnt += 1 
        max_val = max(max_val, node.val)

        for next_node in [node.left, node.right]:
            if not next_node:
                continue 
            self.dfs(next_node, max_val)

            



        
        