# O(N)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            value = carry

            if l1:
                value += l1.val
                l1 = l1.next
            
            if l2:
                value += l2.val
                l2 = l2.next
            
            current.next = ListNode(value % 10)
            current = current.next
            carry = value // 10
        
        return dummy.next
        