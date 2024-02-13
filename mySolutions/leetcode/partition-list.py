# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        temp1 = final1 = ListNode(0)
        temp2 = final2 = ListNode(0)

        curr = head
        while curr:
            if curr.val < x:
                temp1.next = curr
                temp1 = temp1.next
            else:
                temp2.next = curr
                temp2 = temp2.next
            
            curr = curr.next
        temp2.next = None
        temp1.next = final2.next
        return final1.next



