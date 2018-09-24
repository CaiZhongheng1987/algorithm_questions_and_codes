# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []

        result_list = []
        # 采用递归方式来生成所有正确的组合
        Solution.generate_function(self, result_list, '', n, n)

        return result_list

    def generate_function(self, result_list, father_string, left_string, right_string):
        if (left_string == 0) and (right_string == 0):
            result_list.append(father_string)

        if left_string > 0:
            # 在任何时候，只要手里还有左括号，都可以出左括号
            Solution.generate_function(self, result_list, father_string+'(', left_string-1, right_string)

        if right_string > 0 and left_string < right_string:
            # 只有在手上还有右括号，且剩下的右括号比左括号多的情况下，才能出右括号
            Solution.generate_function(self, result_list, father_string + ')', left_string, right_string-1)


test_num = 4

my_test = Solution()
out_list = my_test.generateParenthesis(test_num)
print(out_list)
