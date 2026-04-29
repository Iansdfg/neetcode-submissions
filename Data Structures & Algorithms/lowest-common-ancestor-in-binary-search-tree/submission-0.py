# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        found_p, found_q, lca = self.dfs(root,q,p)
        return lca

    def dfs(self, node, p, q):
        #return found_p, found_q, lca
        if not node:
            return False, False, None 

        left_found_p, left_found_q, left_lca = self.dfs(node.left, p, q)
        right_found_p, right_found_q, right_lca = self.dfs(node.right, p, q)

        if left_lca or right_lca:
            return True, True, left_lca or right_lca 

        found_p = left_found_p or right_found_p or node.val == p.val
        found_q = left_found_q or right_found_q or node.val == q.val

        if found_p and found_q:
            return found_p, found_q, node 

        return found_p, found_q, None 
        

        


        