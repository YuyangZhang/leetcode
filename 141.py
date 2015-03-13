# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        cur=head
        while 1:
            if cur==None:
                return False
            else:
                if cur.val=='##':
                    return True
                else:
                    cur.val='##'
                    cur=cur.next
