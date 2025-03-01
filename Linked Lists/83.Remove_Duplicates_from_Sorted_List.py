# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(N)
    # 2 pointers
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        pos1, pos2 = head, head.next
        while pos2:
            if pos1.val == pos2.val:
                pos1.next = pos2.next
                pos2 = pos2.next
            else:
                pos1 = pos1.next
                pos2 = pos2.next

        return head
    
    
    # O(N)
    # 1 pointer
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pos = head
        while pos and pos.next:
            if pos.val == pos.next.val:
                pos.next = pos.next.next
            else:
                pos = pos.next
        
        return head    
