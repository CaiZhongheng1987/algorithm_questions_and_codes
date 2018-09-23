# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        h = ListNode(-999)
        h.next = head
        p, q = h, h

        for _ in range(n+1):
            q = q.next

        while q is not None:
            q = q.next
            p = p.next

        p.next = p.next.next
        return h.next


class ListNode:
    # 节点初始化
    def __init__(self, value=None, p=None):
        self.val = value
        self.next = p

    def create(self, node_value_list):
        if node_value_list:
            self.val = node_value_list[0]
            tmp_p = self
            for value in node_value_list[1:]:
                tmp_p.next = ListNode(value)
                tmp_p = tmp_p.next

        return self


# main test script
list_1 = [1, 2, 3, 4, 5]

my_list_1 = ListNode()
my_list_1.create(list_1)

remove_number = 2
my_test = Solution()

out_list_node = my_test.removeNthFromEnd(my_list_1, remove_number)
tmp_print = out_list_node
while tmp_print is not None:
    print(tmp_print.val)
    tmp_print = tmp_print.next
