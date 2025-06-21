# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        a=head
        arr=[]
        while a:
            arr.append(a.val)
            a=a.next
        d=deque(arr)
        d.rotate(k)
        res=list(d)
        print(res)
        head1=ListNode(res[0])
        mover=head1
        for i in range(1,len(res)):
            temp=ListNode(res[i])
            mover.next=temp
            mover=mover.next
        return head1
        