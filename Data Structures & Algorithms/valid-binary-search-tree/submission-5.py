# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        is_valid, max_val, min_val = self.dfs(root)
        return is_valid

    def dfs(self, node):
        #return is_valid, max_val, min_val 

        if not node:
            return True, float('-inf'), float('inf')

        left_is_valid, left_max_val , left_min_val= self.dfs(node.left)
        right_is_valid, right_max_val, right_min_val = self.dfs(node.right)

        bst_valid = (left_max_val < node.val) and (right_min_val > node.val)
        is_valid = bst_valid and left_is_valid and right_is_valid
        if not is_valid:
            return False, 0, 0
        max_val = max(left_max_val, right_max_val, node.val)
        min_val = min(left_min_val, right_min_val, node.val)

        return is_valid, max_val, min_val