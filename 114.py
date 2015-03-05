# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root ==None or:
            return
        
        q=[]
        
        result=[]
        q.append(root)
        while q!=[]:
            node=q.pop()
            result.append(node.val)
            if node.right!=None:
                q.append(node.right)
            if node.left!=None:
                q.append(node.left)
        print(result)
        root.right=TreeNode(result[1])
        root.left=None
        cur=root.right
        for i in range(2,len(result)):
            cur.right=TreeNode(result[i])
            cur=cur.right
        node=root
        while node!=None:
            print(node.val)
            node=node.right
root=TreeNode(1)
left=TreeNode(2)
right=TreeNode(5)
leftleft=TreeNode(3)
leftright=TreeNode(4)
rightright=TreeNode(6)
#root.left=left
#root.right=right
#left.left=leftleft
#left.right=leftright
#right.right=rightright
Solution().flatten(root)


