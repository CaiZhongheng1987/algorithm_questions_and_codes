# 给定一个字符串 s 和一些长度相同的单词 words。在 s 中找出可以恰好串联 words 中所有单词的子串的起始位置。
#
# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
#
# 示例 1:
#
# 输入:
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# 输出: [0,9]
# 解释: 从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
# 示例 2:
#
# 输入:
#   s = "wordgoodstudentgoodword",
#   words = ["word","student"]
# 输出: []


class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or words == []:
            return []

        len_s = len(s)
        len_word = len(words[0])  # 注意words里面每个单词的长度相同
        len_words = len(words)  # words里面有多少个单词
        len_sub_s = len_word * len_words  # 子串的总长度
        word_times = dict()
        index_list = []

        for word in words:
            if word in word_times:
                word_times[word] += 1
            else:
                word_times[word] = 1

        for idx in range(0, min(len_word, len_s-len_sub_s+1)):
            # 每个单词长度都是len_word，那就说明只需要选择从0:len_word-1为起点进行遍历即可
            # 遍历的起点就是idx
            cur_dict = dict()
            acc_word_cnt = 0
            for search_idx in range(idx, len_s-len_word+1, len_word):
                if s[search_idx:search_idx+len_word] in word_times:
                    acc_word_cnt += 1
                    if s[search_idx:search_idx+len_word] in cur_dict:
                        cur_dict[s[search_idx:search_idx+len_word]] += 1
                    else:
                        cur_dict[s[search_idx:search_idx+len_word]] = 1
                else:
                    cur_dict.clear()  # 一旦过程中发现有不匹配的字符，就把cur_dict清空
                    acc_word_cnt = 0

                if acc_word_cnt >= len_words:
                    if acc_word_cnt > len_words:
                        # 如果子串匹配word的个数足够多，那就要把最远的一个word丢掉，再比较cur_dict是否和word_times相等
                        tmp_str = s[search_idx-len_sub_s:search_idx+len_word-len_sub_s]
                        cur_dict[tmp_str] -= 1
                    if cur_dict == word_times:
                        index_list.append(search_idx+len_word-len_sub_s)

        return index_list


# main test script
test_s = "barfoofoobarthefoobarman"
test_words = ["bar", "foo", "the"]
my_test = Solution()

return_list = my_test.findSubstring(test_s, test_words)
print(return_list)
