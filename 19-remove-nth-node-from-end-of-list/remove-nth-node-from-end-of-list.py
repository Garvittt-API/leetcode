class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        
        return dummy.next