# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
# 示例:
#
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。


class Solution:
    def letterCombinations(self, digits):
        if digits == '':
            return []

        digits_dict = dict()
        digits_dict['2'] = ['a', 'b', 'c']
        digits_dict['3'] = ['d', 'e', 'f']
        digits_dict['4'] = ['g', 'h', 'i']
        digits_dict['5'] = ['j', 'k', 'l']
        digits_dict['6'] = ['m', 'n', 'o']
        digits_dict['7'] = ['p', 'q', 'r', 's']
        digits_dict['8'] = ['t', 'u', 'v']
        digits_dict['9'] = ['w', 'x', 'y', 'z']

        tmp_out_list = []
        len_digits = len(digits)
        idx_max_list = [3] * len_digits
        iter_num = 1
        idx_list = [0] * len_digits
        digits_list = []

        for idx in range(len_digits):
            digits_list.append(digits_dict[digits[idx]])
            if digits[idx] in ['7', '9']:
                idx_max_list[idx] = 4
                iter_num *= 4
            else:
                iter_num *= 3

        iter_idx = 0
        while iter_idx < iter_num:
            tmp_out_str = ''
            for idx in range(len_digits-1, -1, -1):
                if idx_list[idx] == idx_max_list[idx]:
                    idx_list[idx] = 0
                    idx_list[idx - 1] += 1

                tmp_out_str = digits_list[idx][idx_list[idx]] + tmp_out_str

                if idx == 0:
                    idx_list[-1] += 1

            iter_idx += 1
            tmp_out_list.append(tmp_out_str)

        return tmp_out_list


test_digit_str = '23'

my_test = Solution()
out_list = my_test.letterCombinations(test_digit_str)
print(out_list)
