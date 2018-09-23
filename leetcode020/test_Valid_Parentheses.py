# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
# 示例 3:
#
# 输入: "(]"
# 输出: false
# 示例 4:
#
# 输入: "([)]"
# 输出: false
# 示例 5:
#
# 输入: "{[]}"
# 输出: true


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 利用堆栈来实现括号字符串的匹配
        # 这里利用list来实现简单的堆栈
        if s == '':
            return True

        theses_list = []
        for value in s:
            if value in ['(', '[', '{']:
                theses_list.append(value)  #入栈
                continue
            if value == ')':
                if theses_list == [] or theses_list.pop() != '(':
                    return False
                else:
                    continue
            if value == ']':
                if theses_list == [] or theses_list.pop() != '[':
                    return False
                else:
                    continue
            if value == '}':
                if theses_list == [] or theses_list.pop() != '{':
                    return False
                else:
                    continue

        if theses_list:
            return False
        else:
            return True


test_str = '[]'
my_test = Solution()

out_bool = my_test.isValid(test_str)
print(out_bool)
