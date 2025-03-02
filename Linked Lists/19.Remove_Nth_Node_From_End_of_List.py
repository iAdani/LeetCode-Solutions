# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(N)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pos = head
        length = 0
        while pos:
            pos = pos.next
            length += 1

        pos = dummy
        for _ in range(length - n):
            pos = pos.next
        
        pos.next = pos.next.next
        return dummy.next

    # O(N)
    # Better approach
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        ahead = behind = dummy

        for _ in range(n + 1):
            ahead = ahead.next
        
        while ahead:
            ahead = ahead.next
            behind = behind.next
        
        behind.next = behind.next.next
        return dummy.next
