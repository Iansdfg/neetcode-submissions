# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = self.inorder(root, k)
        return res 
        

    def inorder(self, node, k):
        dummy = TreeNode(-1)
        dummy.right = node
        curr = dummy
        stack = [dummy]
        
        for _ in range(k + 1):
            curr = stack.pop()
            res = curr.val

            curr = curr.right
            while curr:
                stack.append(curr)
                curr = curr.left 

        return res 



        
        