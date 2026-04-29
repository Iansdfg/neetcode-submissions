# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        queue = deque([root])
        res = []
        while queue:
            curr = queue.popleft()
            if curr:
                queue.append(curr.left)
                res.append(str(curr.val))
                queue.append(curr.right)
            else:
                res.append('#')
        res = ",".join(res)
        return res


        

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        data = data.split(",")
        node_list = []
        for dateam in data:
            if dateam == "#":
                node_list.append(None)
            else:
                node_list.append(TreeNode(int(dateam)))
        slow, fast = 0, 1 
        while fast+1 < len(node_list):

            if node_list[slow]:
                curr_node = node_list[slow]
                curr_node.left = node_list[fast]
                curr_node.right = node_list[fast + 1]
                fast += 2
                
            slow += 1 
            
        return node_list[0]
