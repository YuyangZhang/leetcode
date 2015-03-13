# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        cur=head
        while 1:
            if cur==None:
                return None
            else:
                if cur.val=='##':
                    return cur
                else:
                    cur.val='##'
                    cur=cur.next
