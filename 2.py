class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        i1=1
        i2=1
        num1=0
        num2=0
        while True:
            num1+=l1.val*i1
            if l1.next==None:
                break
            else:
                l1=l1.next
                i1*=10
        while True:
            num2+=l2.val*i2
            if l2.next==None:
                break
            else:
                l2=l2.next
                i2*=10
        num=num1+num2
        print(num)
        pre=ListNode(num%10)
        l=pre
        for i in range(1,len(str(num))):
            cur=ListNode(int(str(num)[-1-i]))
            pre.next=cur
            pre=cur
        return l
       
s=Solution()
l1=ListNode(1)
l1.next=ListNode(8)

l2=ListNode(1)
l2.next=ListNode(9)

s.addTwoNumbers(l1,l2)
