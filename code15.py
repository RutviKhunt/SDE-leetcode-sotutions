# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Helper to check if we have at least k nodes
        def has_k_nodes(node, k):
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            return count == k
        
        # Helper to reverse k nodes
        def reverse_k_nodes(head, k):
            prev, curr = None, head
            while k > 0:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                k -= 1
            return prev, curr  # new head, next node after reversed group
        
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while has_k_nodes(group_prev.next, k):
            group_head = group_prev.next
            new_head, next_group = reverse_k_nodes(group_head, k)
            
            # Connect previous part with reversed group
            group_prev.next = new_head
            group_head.next = next_group
            
            # Move pointer
            group_prev = group_head
        
        return dummy.next
