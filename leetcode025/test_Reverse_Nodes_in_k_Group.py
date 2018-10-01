# 给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。
#
# 示例 :
#
# 给定这个链表：1->2->3->4->5
#
# 当 k = 2 时，应当返回: 2->1->4->3->5
#
# 当 k = 3 时，应当返回: 3->2->1->4->5
#
# 说明 :
#
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head

        if head.next is None:
            return head

        # 需要用两个指针，用于标识翻转的起点位置和终点位置
        after_p = ListNode(-2)
        after_p.next = head
        new_head = after_p
        before_p = after_p

        # 初始阶段before和after两个指针位置相同
        # 进行过程中，after先不动，before先走k

        while before_p.next is not None:
            acc_num = 0
            while 1:
                before_p = before_p.next
                acc_num += 1
                if before_p.next is None and acc_num != k:
                    return new_head.next
                if acc_num == k:
                    after_p, before_p = Solution.reverseOneGroup(self, after_p, before_p, k)
                    break

        return new_head.next

    def reverseOneGroup(self, fst_p, sec_p, k):
        tmp_p1 = sec_p.next # 先把最后面的结点指向的下一个位置保存起来
        cur_p = fst_p.next

        for _ in range(k-1):
            tmp_p3 = cur_p.next
            cur_p.next = tmp_p3.next
            tmp_p3.next = fst_p.next
            fst_p.next = tmp_p3

        cur_p.next = tmp_p1
        fst_p = sec_p = cur_p
        return fst_p, sec_p


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
list_1 = [1, 2, 3, 4, 5, 6, 7]

my_list_1 = ListNode(None)
my_list_1.create(list_1)

my_test = Solution()

out_list_node = my_test.reverseKGroup(my_list_1, 3)
tmp_print = out_list_node
while tmp_print is not None:
    print(tmp_print.val)
    tmp_print = tmp_print.next
