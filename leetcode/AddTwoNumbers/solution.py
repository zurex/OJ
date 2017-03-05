# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getVal(self, node):
        """
        :type node: ListNode
        """
        val = node.val
        index = 1
        while node.next:
            node = node.next
            val = val + node.val * pow(10, index)
            index += 1
        return val

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = self.getVal(l1)
        b = self.getVal(l2)
        val = a + b
        bit = val % 10
        val = val / 10
        node = ListNode(bit)
        head = node
        while val > 0:
            prev = node
            bit = val % 10
            node = ListNode(bit)
            prev.next = node
            val = val /10
        return head

def main():
    li1 = ListNode(2)
    li1.next = ListNode(4)
    li1.next.next = ListNode(3)
    li2 = ListNode(5)
    li2.next = ListNode(6)
    li2.next.next = ListNode(4)
    sol = Solution()
    result = sol.addTwoNumbers(li1, li2)
    print result.val
    if result.next:
        result = result.next
        print result.val
    print result.next.val

if __name__ == '__main__':
    main()
    