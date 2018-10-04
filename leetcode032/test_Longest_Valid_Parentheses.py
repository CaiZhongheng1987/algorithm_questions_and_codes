# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
#
# 示例 1:
#
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 示例 2:
#
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        idx_stack = [-1]
        str_stack = []
        len_s = len(s)
        if len_s == 0:
            return 0

        # 有效括号对的边缘有几种情况
        # 首先用堆栈将整个字符串遍历一遍，左括号入栈，右括号出栈
        # 等遍历完成后，查看堆栈中剩余的元素和len_s-1之间的差，找出最大的差，就是最大有效括号对
        str_stack.append(s[0])
        idx_stack.append(0)
        idx = 1
        while idx < len_s:
            if s[idx] is ')' and not str_stack:
                # str_stack为空的情况下，只能直接存入右括号
                str_stack.append(s[idx])
                idx_stack.append(idx)
            elif s[idx] is ')' and str_stack[-1] is '(':
                # 消去有效括号对
                str_stack.pop()
                idx_stack.pop()
            else:
                # 存储不能配对的右括号和初次出现的左括号
                str_stack.append(s[idx])
                idx_stack.append(idx)
            idx += 1

        if not idx_stack:
            return len_s
        else:
            # 遍历完成后，提取idx_stack里面的元素，做等差数列，然后找最大值
            # idx_stack里面的元素就是有效括号
            idx_stack.append(len_s)
            tmp_idx_stack = idx_stack[1:]
            tmp_idx_stack.append(0)
            diff_list = [tmp_idx_stack[i] - idx_stack[i] - 1 for i in range(len(tmp_idx_stack))]
            diff_list.pop()
            return max(diff_list)


# main test script
test_str = "()()())"
my_test = Solution()

len_parentheses = my_test.longestValidParentheses(test_str)
print(len_parentheses)
