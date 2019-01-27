# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
#
# 如果不存在最后一个单词，请返回 0 。
#
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
#
# 示例:
#
# 输入: "Hello World"
# 输出: 5


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        len_s = len(s)
        word_end = 0
        word_exist_flag = 0
        for idx in range(len_s-1, -1, -1):
            if s[idx] is ' ' and word_exist_flag is 0:
                continue
            elif s[idx] is not ' ' and word_exist_flag is 0:
                word_end = idx
                word_exist_flag = 1
            elif s[idx] is not ' ' and word_exist_flag is 1:
                continue
            else:
                # s[idx] is ' ' and word_exist_flag is 1:
                return word_end-idx

        if word_exist_flag is 1:
            return word_end+1
        else:
            return 0


if __name__ == '__main__':
    input_string = '   b   '
    my_test = Solution()
    return_string = my_test.lengthOfLastWord(input_string)
    print(return_string)
