# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
# 示例:
#
# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        if m == 0:
            return None
        n = len(grid[0])
        if n == 0:
            return None
        if m == n == 1:
            return grid[0][0]

        # 使用动态规划来完成这道题
        # 参考leetcode062的代码
        path_dict = dict()
        path_dict[(1, 1)] = grid[-1][-1]
        return self.path_nums(m, n, path_dict, grid, m, n)

    def path_nums(self, x, y, path_dict, grid, m, n):
        if (x, y) in path_dict:
            pass
        elif x is 1:
            # 行向量
            path_dict[(x, y)] = grid[m-x][n-y] + self.path_nums(x, y-1, path_dict, grid, m, n)
        elif y is 1:
            # 列向量
            path_dict[(x, y)] = grid[m-x][n-y] + self.path_nums(x-1, y, path_dict, grid, m, n)
        else:
            # 递归调用
            path_dict[(x, y)] = min(self.path_nums(x - 1, y, path_dict, grid, m, n),
                                    self.path_nums(x, y - 1, path_dict, grid, m, n)) + grid[m-x][n-y]

        return path_dict[(x, y)]


if __name__ == '__main__':
    input_matrix = [
                      [1,3,1],
                      [1,5,1],
                      [4,2,1]
                   ]

    my_test = Solution()
    paths = my_test.minPathSum(input_matrix)
    print(paths)
