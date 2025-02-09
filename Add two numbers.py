class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s=ListNode(0)
        ptr=s
        c=0
        while l1 or l2 or c:
            if l1:
                c+=l1.val
                l1=l1.next
            if l2:
                c+=l2.val
                l2=l2.next
            ptr.next=ListNode(c%10)
            ptr=ptr.next
            c=c//10
        return s.next    

        
