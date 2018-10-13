# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用一次。
#
# 说明：
#
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。
# 示例 1:
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# 示例 2:
#
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
#   [1,2,2],
#   [5]
# ]


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # 还是使用动态规划来解决
        # 在编号039的题目上加入两点新设定
        # 1、每次选取can[idx+1:]的数，不包含当前idx，因为该题要求每个数字在每个组合中只能使用一次。
        # 2、for循环每次需要跳过重复的数字，因为前面的数字已经包含了所有可能性的结果
        if candidates is []:
            return []

        candidates.sort()
        result_list = self.dp_design(candidates, target)
        return result_list

    def dp_design(self, candidates, target):
        sub_list = []
        for idx in range(len(candidates)):
            tmp_can = candidates[idx]
            if idx > 0 and tmp_can == candidates[idx-1]:
                continue
            else:
                if tmp_can < target:
                    tmp_list = self.dp_design(candidates[idx+1:], target - tmp_can)
                    for tmp_val in tmp_list:
                        tmp_val.append(tmp_can)
                        sub_list.append(tmp_val)
                elif tmp_can == target:
                    sub_list.append([tmp_can])
                else:
                    break

        return sub_list


# main test script
test_list = [2, 5, 2, 1, 2]
test_target = 5

my_test = Solution()
out_list = my_test.combinationSum2(test_list, test_target)
print(out_list)
