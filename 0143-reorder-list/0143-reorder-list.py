# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
            
        curr = head
        for i in range(len(values)):
            if i%2 == 0:
                curr.val = values[i//2]
            else:
                curr.val = values[len(values)-(i+1)//2]
            curr = curr.next