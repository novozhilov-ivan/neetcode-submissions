
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        #1
        left_prev, cur = dummy, head
        for i in range(left - 1):
            left_prev, cur = cur, cur.next
        
        # 2
        prev = None
        for i in range(right - left + 1):
            temp = cur.next 
            cur.next = prev
            prev, cur = cur, temp
        
        #3 
        left_prev.next.next = cur
        left_prev.next = prev
        return dummy.next       
