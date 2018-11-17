# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
# 示例:
#
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# 说明：
#
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 建立一个字典来存储每个字符串的字母，key值为排序后的字符串，
        # value值为没做排序的字符串，这样就可以把字母相同的字符串归类到一起
        dict_list = dict()

        for tmp_string in strs:
            sort_string = ''.join(sorted(tmp_string))
            if sort_string in dict_list:
                dict_list[sort_string].append(tmp_string)
            else:
                dict_list[sort_string] = [tmp_string]

        return list(dict_list.values())


input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]

my_test = Solution()
output_list = my_test.groupAnagrams(input_list)
print(output_list)
