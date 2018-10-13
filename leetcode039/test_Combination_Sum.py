# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。
# 示例 1:
#
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
#   [7],
#   [2,2,3]
# ]
# 示例 2:
#
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # 使用动态规划来解决
        # 设计dp[i]为target为i的集合
        # 那么dp[8]就是(2, dp[6])+(3, dp[5])+(5, dp[3])的组合，剩下的可以以此类推
        # 每次加入的时候需要排除重复项，所以直接用dp的话会有一定程度的冗余
        # 一个解决办法是先对数组进行排序，然后用dp的时候只选择当前idx和idx之后的数组进行查找
        # 比如上面的(3, dp[5])，做dp[5]的时候就只用[3, 5]，因为涉及到2的结果在(2, dp[6])的时候已经列举完全了
        # 这样就避免了重复结果排序然后消除相同项的问题
        if candidates is []:
            return []

        candidates.sort()
        result_list = self.dp_design(candidates, target)
        return result_list

    def dp_design(self, candidates, target):

        if candidates[0] > target:
            return []

        sub_list = []
        for idx in range(len(candidates)):
            tmp_can = candidates[idx]
            if tmp_can < target:
                tmp_list = self.dp_design(candidates[idx:], target - tmp_can)
                for tmp_val in tmp_list:
                    tmp_val.append(tmp_can)
                    sub_list.append(tmp_val)
            elif tmp_can == target:
                sub_list.append([tmp_can])
            else:
                break

        return sub_list


# main test script
test_list = [2, 3, 5]
test_target = 8

my_test = Solution()
out_list = my_test.combinationSum(test_list, test_target)
print(out_list)
