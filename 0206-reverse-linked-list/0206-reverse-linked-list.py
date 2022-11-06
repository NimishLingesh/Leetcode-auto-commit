# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
            
        ret = head
        head = head.next
        ret.next = None
        
        while head != None:
            first = head
            head = head.next
            first.next = ret
            ret = first
        return ret