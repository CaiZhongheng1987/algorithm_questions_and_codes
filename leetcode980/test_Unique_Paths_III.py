# 在二维网格grid上，有4种类型的方格：
#
# 1表示起始方格。且只有一个起始方格。
# 2表示结束方格，且只有一个结束方格。
# 0表示我们可以走过的空方格。
# -1表示我们无法跨越的障碍。
# 返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目，每一个无障碍方格都要通过一次。
#
# 示例1：
# 输入：[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
# 输出：2
# 解释：我们有以下两条路径：
# 1.(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2)
# 2.(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (2, 2)
#
# 示例2：
# 输入：[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
# 输出：4
# 解释：我们有以下四条路径：
# 1.(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)
# 2.(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 3), (1, 3), (2, 3)
# 3.(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (1, 1), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3)
# 4.(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (2, 2), (2, 3)
#
# 示例3：
# 输入：[[0, 1], [2, 0]]
# 输出：0
# 解释：
# 没有一条路能完全穿过每一个空的方格一次。
# 请注意，起始和结束方格可以位于网格中的任意位置。
#
# 提示：
# 1 <= grid.length * grid[0].length <= 20


class Solution:
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # 仍然用动态规划来解决这道题
        m = len(grid)
        n = len(grid[0])
        if m == n == 1:
            return 0
        grid_num = m*n
        m -= 1
        n -= 1

        # 建立可用格子的字典，用于保存已经使用过的格子
        grid_dict = dict()
        # 建立另外一个字典，用于保存当前已经用过的所有格子
        # key包含两个值，第一个是当前所有坐标转为一维坐标out=row_num*(n+1)+col_num，。然后用不超过20bit的非负整数来实现
        # 为了保存历史状态，这个值需要和历史状态相加
        # 第二个值，是当前路线所处的坐标，也转换为out=row_idx*(n+1)+col_idx
        dp_dict = dict()

        # 找到起始点1和结束点2所在的位置
        start_row = 0
        start_col = 0
        end_row = 0
        end_col = 0
        for row_idx, row_val in enumerate(grid):
            for col_idx, col_val in enumerate(row_val):
                if grid[row_idx][col_idx] is 1:
                    start_row = row_idx
                    start_col = col_idx
                    grid_dict[(row_idx, col_idx)] = 1
                elif grid[row_idx][col_idx] is 2:
                    end_row = row_idx
                    end_col = col_idx
                elif grid[row_idx][col_idx] is -1:
                    grid_dict[(row_idx, col_idx)] = 1
                else:
                    pass

        path_num = 0
        dp_num = 0
        return self.path_search(start_row, start_col, end_row, end_col, grid_dict, path_num, m, n, grid_num,
                                dp_dict, dp_num)

    def path_search(self, row_num, col_num, end_row, end_col, grid_dict, path_num, m, n, grid_num, dp_dict, dp_num):
        # 先判断终止条件
        if (row_num, col_num) == (end_row, end_col):
            if len(grid_dict) == grid_num:
                # 正确路线
                path_num += 1
            else:
                # 错误路线
                pass
            return path_num

        # 在网格中寻找上下左右的可行路线，注意边界条件

        # 判断是否存在左边的可行网格
        if col_num > 0 and (row_num, col_num-1) not in grid_dict:
            grid_dict[(row_num, col_num-1)] = 1
            tmp_val = row_num*(n+1)+col_num-1
            dp_num += 2**tmp_val
            if (dp_num, tmp_val) in dp_dict:
                path_num += dp_dict[(dp_num, tmp_val)]
            else:
                add_num = self.path_search(row_num, col_num-1, end_row, end_col, grid_dict, path_num, m, n, grid_num,
                                           dp_dict, dp_num)
                dp_dict[(dp_num, tmp_val)] = add_num-path_num
                path_num = add_num
            del grid_dict[(row_num, col_num-1)]
            dp_num -= 2**tmp_val

        # 判断是否存在右边的可行网格
        if col_num < n and (row_num, col_num+1) not in grid_dict:
            grid_dict[(row_num, col_num+1)] = 1
            tmp_val = row_num*(n + 1)+col_num+1
            dp_num += 2**tmp_val
            if (dp_num, tmp_val) in dp_dict:
                path_num += dp_dict[(dp_num, tmp_val)]
            else:
                add_num = self.path_search(row_num, col_num+1, end_row, end_col, grid_dict, path_num, m, n, grid_num,
                                           dp_dict, dp_num)
                dp_dict[(dp_num, tmp_val)] = add_num-path_num
                path_num = add_num
            del grid_dict[(row_num, col_num+1)]
            dp_num -= 2**tmp_val

        # 判断是否存在上边的可行网格
        if row_num > 0 and (row_num-1, col_num) not in grid_dict:
            grid_dict[(row_num-1, col_num)] = 1
            tmp_val = (row_num-1)*(n+1)+col_num
            dp_num += 2**tmp_val
            if (dp_num, tmp_val) in dp_dict:
                path_num += dp_dict[(dp_num, tmp_val)]
            else:
                add_num = self.path_search(row_num-1, col_num, end_row, end_col, grid_dict, path_num, m, n, grid_num,
                                           dp_dict, dp_num)
                dp_dict[(dp_num, tmp_val)] = add_num-path_num
                path_num = add_num
            del grid_dict[(row_num-1, col_num)]
            dp_num -= 2**tmp_val

        # 判断是否存在下边的可行网格
        if row_num < m and (row_num+1, col_num) not in grid_dict:
            grid_dict[(row_num+1, col_num)] = 1
            tmp_val = (row_num+1)*(n+1)+col_num
            dp_num += 2**tmp_val
            if (dp_num, tmp_val) in dp_dict:
                path_num += dp_dict[(dp_num, tmp_val)]
            else:
                add_num = self.path_search(row_num+1, col_num, end_row, end_col, grid_dict, path_num, m, n, grid_num,
                                           dp_dict, dp_num)
                dp_dict[(dp_num, tmp_val)] = add_num-path_num
                path_num = add_num
            del grid_dict[(row_num+1, col_num)]
            dp_num -= 2**tmp_val

        return path_num


if __name__ == '__main__':
    input_matrix = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
    # input_matrix = [[1, 0, 0], [0, 0, 0], [0, 0, 2]]
    # input_matrix = [[1, 0], [0, 2]]
    my_test = Solution()
    path_nums = my_test.uniquePathsIII(input_matrix)
    print(path_nums)

