# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(N)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        pos1, pos2 = None, head.next
        while pos2:
            head.next = pos1
            pos1 = head
            head = pos2
            pos2 = pos2.next
        
        head.next = pos1
        return head
    

    # O(N)
    # Another version
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        
        return prev
        