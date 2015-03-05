# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        result=[]
        if root==None:
            return result
        indexDic=bfs(root)
        for i in range(0,len(indexDic)):
            if indexDic[len(indexDic)-1-i]!=[]:
                result.append(indexDic[len(indexDic)-i-1])
        return result
def bfs(root):
    indexDic={}
    q=[]
    q.insert(0,root)
    level=0
    nodeNum=1
    index=0
    while q!=[]:
        if level not in indexDic:
            indexDic[level]=[]
        node=q.pop()
        indexDic[level].append(node.val)
        index+=1
        if node.left!=None:
            q.insert(0,node.left)
        if node.right!=None:
            q.insert(0,node.right)
        if index==nodeNum:
            level+=1
            nodeNum=len(q)
            index=0
    return indexDic

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
print(Solution().levelOrderBottom({}))
