# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time: O(N), Space: O(1)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find the middle node
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse the second half
        prev = None
        node = slow
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt

        # Check for palindrome
        end = prev
        while end:
            if head.val != end.val:
                return False
            head = head.next
            end = end.next

        return True
