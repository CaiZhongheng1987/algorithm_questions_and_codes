# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 示例:
#
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
# 说明:
#
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        if head.next is None:
            return head

        cur_p = ListNode(-2)
        cur_p.next = head
        new_head = ListNode(-2)
        new_head.next = cur_p

        while 1:
            tmp_p1 = cur_p.next
            cur_p.next = cur_p.next.next
            tmp_p2 = cur_p.next.next
            cur_p.next.next = tmp_p1
            cur_p.next.next.next = tmp_p2

            cur_p = cur_p.next.next
            if cur_p.next is None:
                break
            if cur_p.next.next is None:
                break

        return new_head.next.next


class ListNode:
    # 节点初始化
    def __init__(self, x):
        self.val = x
        self.next = None

    def create(self, node_value_list):
        if node_value_list:
            self.val = node_value_list[0]
            tmp_p = self
            for value in node_value_list[1:]:
                tmp_p.next = ListNode(value)
                tmp_p = tmp_p.next

        return self


# main test script
list_1 = [1, 2, 3, 4]

my_list_1 = ListNode(None)
my_list_1.create(list_1)

my_test = Solution()

out_list_node = my_test.swapPairs(my_list_1)
tmp_print = out_list_node
while tmp_print is not None:
    print(tmp_print.val)
    tmp_print = tmp_print.next
