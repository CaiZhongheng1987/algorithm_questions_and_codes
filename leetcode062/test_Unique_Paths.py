# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 问总共有多少条不同的路径？
#
#
#
# 例如，上图是一个7 x 3 的网格。有多少可能的路径？
#
# 说明：m 和 n 的值均不超过 100。
#
# 示例 1:
#
# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
# 示例 2:
#
# 输入: m = 7, n = 3
# 输出: 28


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        # 使用动态规划来完成这道题
        if m is 0 or n is 0:
            return 0
        if m == n == 1:
            return 1

        path_dict = dict()
        return self.path_nums(m-1, n, path_dict)+self.path_nums(m, n-1, path_dict)

    def path_nums(self, x, y, path_dict):
        if (x, y) in path_dict:
            pass
        elif x is 1 or y is 1:
            # 行向量和列向量只有一种走法
            path_dict[(x, y)] = 1
        elif x is 0 or y is 0:
            path_dict[(x, y)] = 0
        elif (y, x) in path_dict:
            # 旋转90度对称的网格走法相同
            path_dict[(x, y)] = path_dict[(y, x)]
        else:
            # 递归调用
            path_dict[(x, y)] = self.path_nums(x-1, y, path_dict)+self.path_nums(x, y-1, path_dict)

        return path_dict[(x, y)]


if __name__ == '__main__':
    input_m = 1
    input_n = 1
    my_test = Solution()
    paths = my_test.uniquePaths(input_m, input_n)
    print(paths)

