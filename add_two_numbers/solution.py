# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode()
        root = result

        while l1 or l2:

            first_num = l1.val if l1 and l1.val else 0
            second_num = l2.val if l2 and l2.val else 0

            sum = first_num + second_num + carry
            num = sum % 10
            carry = sum // 10

            result.next = ListNode(val=num)
            result = result.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            result.next = ListNode(carry)

        return root.next


    def print_link_list(self, node):
        linkedListStr = ""
        while node:
            linkedListStr = linkedListStr + str(node.val) + " "
            node = node.next
        print(linkedListStr)

if __name__ == '__main__':
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))

    solution = Solution()

    # solution.print_link_list(l1)
    # l1 = solution.reverse(l1)
    # solution.print_link_list(l1)

    res = solution.addTwoNumbers(l1, l2)
    solution.print_link_list(res)