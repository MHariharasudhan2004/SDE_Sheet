# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l1=head
        arr=deque()
        while l1:
            arr.append(l1.val)
            l1=l1.next
        while len(arr)>1:
            if arr.popleft()!=arr.pop():
                return False
        return True
            
        