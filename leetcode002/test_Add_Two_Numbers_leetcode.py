# 给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
#
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807


class Solution:
    def addTwoNumbers(self, l1, l2):
        new_list = []
        tmp_sum = l1.val + l2.val
        plus_value = tmp_sum // 10
        new_list.append(tmp_sum % 10)
        p_1 = l1.next
        p_2 = l2.next

        while p_1 is not None and p_2 is not None:
            tmp_sum = p_1.val + p_2.val + plus_value
            plus_value = tmp_sum // 10
            new_list.append(tmp_sum % 10)
            p_1 = p_1.next
            p_2 = p_2.next

        if p_1 is None:
            while p_2 is not None:
                tmp_sum = p_2.val + plus_value
                plus_value = tmp_sum // 10
                new_list.append(tmp_sum % 10)
                p_2 = p_2.next
        elif p_2 is None:
            while p_1 is not None:
                tmp_sum = p_1.val + plus_value
                plus_value = tmp_sum // 10
                new_list.append(tmp_sum % 10)
                p_1 = p_1.next

        if plus_value != 0:
            new_list.append(plus_value)

        tmp_self = ListNode(None)
        self = Solution.create(tmp_self, new_list)

        return self

    def create(self, node_value_list):
        if node_value_list:
            self.val = node_value_list[0]
            tmp_p = self
            for value in node_value_list[1:]:
                tmp_p.next = ListNode(value)
                tmp_p = tmp_p.next

        return self


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
list_1 = [2, 4, 3]
list_2 = [5, 6, 9, 6, 7]

my_list_1 = ListNode()
my_list_1.create(list_1)

my_list_2 = ListNode()
my_list_2.create(list_2)

# add_list = Solution()
add_list = ListNode()

add_list = Solution.addTwoNumbers(add_list, my_list_1, my_list_2)
