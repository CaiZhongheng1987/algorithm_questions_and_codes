# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 示例 2:
#
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head or not head.next or k is 0:
            return head

        # 先遍历到链表末尾，顺便记录链表长度
        tail = head
        new_head = head
        len_list_head = 0
        len_flag = 0  # 0表示k小于链表长度，1表示k大于等于链表长度
        for _ in range(0, k):
            if tail.next:
                tail = tail.next
                len_list_head += 1
            else:
                len_list_head += 1
                len_flag = 1
                break

        if len_flag is 0:
            # 双指针遍历到链表尾部和新链表的头部
            len_list_head = k+1
            while tail.next:
                tail = tail.next
                new_head = new_head.next
                len_list_head += 1

            tmp_head = new_head.next
            new_head.next = None
            new_head = tmp_head
            tail.next = head
        else:
            # k大于等于链表长度，先让k对链表长度取余
            k %= len_list_head
            if k is 0:
                return head
            else:
                # 找到第len_list_node-k个节点
                k = len_list_head-k-1
                k_head = head
                for _ in range(0, k):
                    k_head = k_head.next

                tail.next = head
                new_head = k_head.next
                k_head.next = None

        return new_head


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


if __name__ == '__main__':
    list_1 = [1, 2, 3, 4, 5]

    my_list_1 = ListNode()
    my_list_1.create(list_1)

    rotate_number = 3
    my_test = Solution()

    out_list_node = my_test.rotateRight(my_list_1, rotate_number)
    tmp_print = out_list_node
    while tmp_print is not None:
        print(tmp_print.val)
        tmp_print = tmp_print.next
    
