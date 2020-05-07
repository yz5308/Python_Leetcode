# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #判断回文主要是前半部分和后半部分的比较，若能将前半部分压栈，再依次出栈与后半部分比较，则可判断是否回文。
        fast = slow = ListNode(0)
        fast = slow = head
        stack = []

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        while slow:
            top = stack.pop()

            if top != slow.val:
                return False
            slow = slow.next
        return True

class Solution2:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow = slow.next
        slow = self.reverseList(slow)

        while slow:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next
        return True

    def reverseList(self, head):
        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
        return new_head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    print(Solution().isPalindrome(head))






    """
        Time Complexity = O(N)
        Space Complexity = O(n/2)

        Given a singly linked list, determine if it is a palindrome.

        Example:
        Input: 1->2->2->1
        Output: true
    """
