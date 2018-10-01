# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
#
# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return []

        # 先把所有链表的val都灌入一个列表中
        store_list = []
        for node in lists:
            if node and node.val is not None:
                tmp_p = node
                while tmp_p:
                    store_list.append(tmp_p.val)
                    tmp_p = tmp_p.next

        # 将store_list进行排序
        if not store_list:
            return []

        store_list.sort()

        # 将排序后的list组成新的链表
        new_list_node = ListNode(None)
        if store_list:
            new_list_node.val = store_list[0]
            tmp_p = new_list_node
            for value in store_list[1:]:
                tmp_p.next = ListNode(value)
                tmp_p = tmp_p.next

        return new_list_node


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
list_1 = [0, 2, 5]
list_2 = []
list_3 = []


my_list_1 = ListNode(None)
my_list_1.create(list_1)

my_list_2 = ListNode(None)
my_list_2.create(list_2)

my_list_3 = ListNode(None)
my_list_3.create(list_3)

my_test = Solution()

my_lists = [my_list_1, my_list_2, my_list_3]

out_list_node = my_test.mergeKLists(my_lists)
tmp_print = out_list_node
while tmp_print is not None:
    print(tmp_print.val)
    tmp_print = tmp_print.next
