# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        lists=[]
        q=[root]
        remain=sum
        list=[]
        while q!=[]:
            cur=q.pop()
            list.append(cur.val)
            remain-=cur.val
            if cur.left!=None:
                q.append(cur.left)
            if cur.right!=None:
                q.append(cur.right)
            if cur.left==None and cur.right==None:
                if remain==0:
                    lists.append(list)
                    list.pop()
                else:
                    list.pop()
                    print(list)
        return lists
root=TreeNode(1)
root.left=TreeNode(2)
root.left.right=TreeNode(3)
root.right=TreeNode(4)
root.right.right=TreeNode(5)



Solution().pathSum(root,6)

