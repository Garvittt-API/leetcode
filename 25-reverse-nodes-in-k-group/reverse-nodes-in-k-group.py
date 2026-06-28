class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
            
        dummy = ListNode(0, head)
        prev_group = dummy
        
        while True:
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            next_group = kth.next

            prev_node, curr = next_group, prev_group.next
            for _ in range(k):
                temp = curr.next
                curr.next = prev_node
                prev_node = curr
                curr = temp

            temp = prev_group.next
            prev_group.next = kth
            prev_group = temp