# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if height(root)==-1:
            return False
        else:
            return True


def height(root):
    if root==None:
        return 0
    else:
        Hleft=height(root.left)
        Hright=height(root.right)
        if Hleft==-1 or Hright==-1:
            return -1
        else:
            if abs(Hleft-Hright)>1:
                return -1
            else:
                return 1+max(Hleft,Hright)

root=TreeNode(0)
left=TreeNode(0)
right=TreeNode(0)
subleft=TreeNode(0)
subbleft=TreeNode(0)
root.left=left
left.left=subleft
subleft.left=subbleft
root.right=right
s=Solution()
print(s.isBalanced(root))
