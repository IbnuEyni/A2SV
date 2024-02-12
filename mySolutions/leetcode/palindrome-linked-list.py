# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def reverse_list(node):
            prev = None
            curr = node

            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        def middle_node(node):
            slow = fast = node

            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        mid = middle_node(head)
        sec_half =  reverse_list(mid)

        if not head or not head.next:
            return True
            
        while sec_half:
            if head.val != sec_half.val:
                return False
            head = head.next
            sec_half = sec_half.next
        
        return True

