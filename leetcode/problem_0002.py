"""Add two numbers
Two non-negative integers are represented by two non-empty linked list in reverse order.
For example:
    342 is 2 -> 4 -> 3
    465 is 5 -> 6 -> 4
Each node in the list represents a single digit. Two numbers do not contain any leading zero, 
except the number 0 itself.

Output the sum of two numbers. With the example above, the result is 7 -> 0 -> 8.

Constraints:
    - The number of nodes in each list is in the range [1, 100].
    - 0 <= Node.val <= 9.
"""

"""
Using a variable to store the carry and loop through two lists until we reach the end of both.
Using three pointers for the answer, the first, and the second list, respectively.
As we store the first digit in the next node of the answer (p.next = ListNode(s % 10)), 
we should return from ans.next, not the ans pointer itself.

Memory: O(1).
Time: O(max(m, n)) with m is the length of the first list and n is the length of the second list.
"""


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ans = ListNode()
        p, p1, p2 = ans, l1, l2
        carry = 0
        while p1 != None or p2 != None:
            x = 0 if p1 == None else p1.val
            y = 0 if p2 == None else p2.val
            s = x + y + carry
            carry = s // 10
            p.next = ListNode(s % 10)
            p = p.next
            if p1 != None:
                p1 = p1.next
            if p2 != None:
                p2 = p2.next
        if carry > 0:
            p.next = ListNode(carry)

        return ans.next
