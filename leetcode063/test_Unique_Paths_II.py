# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
#
#
#
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
#
# 说明：m 和 n 的值均不超过 100。
#
# 示例 1:
#
# 输入:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        # 使用动态规划来完成这道题，但是要减去障碍物的路径
        # 在leetcode063的基础上修改而成
        path_dict = dict()
        m = len(obstacleGrid)
        if m is 0:
            return 0
        n = len(obstacleGrid[0])
        if m == n == 1:
            if obstacleGrid[0][0] is 0:
                return 1
            else:
                return 0
        m -= 1
        n -= 1
        # 以(0,0)为起始点坐标，目标是走到(m,n)的位置
        return self.path_nums(0, 0, path_dict, obstacleGrid, m, n)

    def path_nums(self, x, y, path_dict, obstacleGrid, m, n):
        if (x, y) in path_dict:
            pass
        elif y is m:
            # 行向量在没有遇到障碍物时，只有一种走法
            if 1 in obstacleGrid[-1][x:]:
                path_dict[(x, y)] = 0
            else:
                path_dict[(x, y)] = 1
        elif x is n:
            # 列向量在没有遇到障碍物时，只有一种走法
            tmp_list = [val[-1] for idx, val in enumerate(obstacleGrid) if idx >= y]
            if 1 in tmp_list:
                path_dict[(x, y)] = 0
            else:
                path_dict[(x, y)] = 1
        else:
            # 递归调用
            # print(x, y)
            if obstacleGrid[y][x] is 1:
                path_dict[(x, y)] = 0
            else:
                path_dict[(x, y)] = (self.path_nums(x+1, y, path_dict, obstacleGrid, m, n)
                                     + self.path_nums(x, y+1, path_dict, obstacleGrid, m, n))

        return path_dict[(x, y)]


if __name__ == '__main__':
    # input_matrix = [
    #                   [0,0,0],
    #                   [0,0,1],
    #                   [0,0,0]
    #                ]
    # input_matrix = [[0, 0], [0, 1], [0, 0]]
    input_matrix = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0],
     [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0],
     [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    my_test = Solution()
    paths = my_test.uniquePathsWithObstacles(input_matrix)
    print(paths)
