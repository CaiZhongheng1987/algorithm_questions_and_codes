# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None and l2 is None:
            return None

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        l_out = ListNode(None)
        p_l1 = l1
        p_l2 = l2

        if p_l1.next is None and p_l2.next is None:
            l_out.val = min(p_l1.val, p_l2.val)
            l_out.next = ListNode(None)
            l_out.next.val = max(p_l1.val, p_l2.val)
            l_out.next.next = None
            return l_out

        p_l_out = l_out
        while 1:
            if p_l1 is None:
                p_l_out.val = p_l2.val
                p_l_out.next = p_l2.next
                return l_out
            elif p_l2 is None:
                p_l_out.val = p_l1.val
                p_l_out.next = p_l1.next
                return l_out
            else:
                pass

            if p_l1.val <= p_l2.val:
                p_l_out.val = p_l1.val
                p_l1 = p_l1.next
            else:
                p_l_out.val = p_l2.val
                p_l2 = p_l2.next

            p_l_out.next = ListNode(None)
            p_l_out = p_l_out.next



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
list_1 = [1, 2, 4]
list_2 = [1, 3, 4]


my_list_1 = ListNode(None)
my_list_1.create(list_1)

my_list_2 = ListNode(None)
my_list_2.create(list_2)

my_test = Solution()

out_list_node = my_test.mergeTwoLists(my_list_1, my_list_2)
tmp_print = out_list_node
while tmp_print is not None:
    print(tmp_print.val)
    tmp_print = tmp_print.next
