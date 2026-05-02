# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        found_LCA = self.find_LCA(root, p, q)

        return found_LCA

    def find_LCA(self, node, p, q):
        if not node:
            return None

        left_found_candidit = self.find_LCA(node.left, p, q)
        right_found_candidit = self.find_LCA(node.right, p, q)

    
        if left_found_candidit and right_found_candidit:
            return node
        if node.val == p.val or node.val == q.val:
            return node
            
        if left_found_candidit or right_found_candidit:
            return left_found_candidit or right_found_candidit

    