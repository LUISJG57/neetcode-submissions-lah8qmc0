# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        aux = []
        curr = head
        while curr:
            aux.append(curr.val)
            curr = curr.next
        print(aux)

        if len(aux) == 1:
            return None

        index = len(aux) - n
        aux.pop(index)
        
        print(aux)
        dummy = ListNode(0)
        res = dummy
        for num in aux:
            res.next = ListNode(num)
            res = res.next
        print(res)
        return dummy.next
       
        