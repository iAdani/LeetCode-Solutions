# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(N)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        head, pos = None, None
        if list1.val > list2.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next
        
        pos = head
        while list1 and list2:
            if list1.val > list2.val:
                pos.next = list2
                list2 = list2.next
            else:
                pos.next = list1
                list1 = list1.next
            
            pos = pos.next

        if list1:
            pos.next = list1
        if list2:
            pos.next = list2

        return head


    # O(N)
    # Another version that apperantly runs slower
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            pos = dummy

            while list1 and list2:
                if list1.val < list2.val:
                    pos.next = list1
                    list1 = list1.next
                else:
                    pos.next = list2
                    list2 = list2.next
                
                pos = pos.next
            
            pos.next = list1 if list1 else list2

            return dummy.next
        