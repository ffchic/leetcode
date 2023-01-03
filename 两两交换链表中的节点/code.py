# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 循环
    def swapPairs(self, head):
        res = ListNode()
        res.next = head
        cur = res
        while cur.next != None and cur.next.next != None:
            nex = head.next
            tmp = nex.next
            nex.next = head
            cur.next = nex
            head.next = tmp
            cur = head
            head = head.next
        return res.next


class Solution2:
    # 递归
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        nex = head.next
        head.next = self.swapPairs(nex.next)
        nex.next = head
        return nex