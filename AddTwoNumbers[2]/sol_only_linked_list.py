from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = res_r = ListNode(0)
        carry = 0
        while l1 and l2:
            res_r.next = ListNode((l1.val + l2.val + carry)%10)
            carry = (l1.val + l2.val + carry)//10
            l1, l2, res_r = l1.next, l2.next, res_r.next
        
        if l1 or l2:
            l_rest = l1 if l1 else l2
            while l_rest:
                res_r.next = ListNode((l_rest.val + carry)%10)
                carry = (l_rest.val + carry)//10
                l_rest, res_r = l_rest.next, res_r.next
        if carry:
            res_r.next = ListNode(1)
        return res.next