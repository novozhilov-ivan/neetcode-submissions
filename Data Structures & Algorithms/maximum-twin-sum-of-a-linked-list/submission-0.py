# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        first, second = head, slow.next if slow.next else slow

        res = 0
        while first and second:
            res = max(res, first.val + second.val)
            first, second = first.next, second.next
        
        return res
