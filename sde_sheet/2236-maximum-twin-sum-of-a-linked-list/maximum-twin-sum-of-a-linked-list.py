# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head.next
        st=[]
        st.append(slow.val)
        while fast.next:
            slow=slow.next
            fast=fast.next.next
            st.append(slow.val)
        twinMax=-9999
        while slow.next:
            slow=slow.next
            prevVal=st.pop()
            twinMax=max(twinMax,prevVal+slow.val)
        return twinMax
        