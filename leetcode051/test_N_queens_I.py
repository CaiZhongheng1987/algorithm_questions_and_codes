# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

# 上图为 8 皇后问题的一种解法。
#
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
#
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
# 示例:
#
# 输入: 4
# 输出: [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
import time


class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        # 将棋盘变为一维序列，建立字典表明棋盘每个格子的是否可用，如果为1，就表明可用，为0则表示不可用。
        # 采用深度遍历搜索方式

        grid_state = dict()
        # 初始化字典，将棋盘上所有格子的状态设置为1
        # 棋盘优先遍历行，变为一维数组
        for idx in range(n**2):
            grid_state[idx] = 1

        # 皇后一共有n个，这里用递归函数来实现
        result_list = []  # 建立解法的list
        chess_board = ['.']*(n**2)  # 建立棋盘，默认全用.来填充

        self.search_answer(grid_state, n, 0, result_list, chess_board, n**2, n)
        return result_list

    def search_answer(self, grid_state, res_n, start_idx, result_list, chess_board, len_grid, n):
        if res_n == 0:
            # 表明所有的n已经用完，且找到了正确的解答
            # return_flag = True
            # 记录下此时的chess_board
            tmp_result = []

            for idx in range(n):
                row_start = idx*n
                row_end = (idx+1)*n
                tmp_result.append(''.join(chess_board[row_start:row_end]))

            result_list.append(tmp_result)
            return None

        # 判断grid_state是否都为0，如果都为0，就说明棋盘上已经放不下皇后了
        if not any(grid_state.values()):
            # 放不下新的皇后
            return None
        else:
            # 接下来进行递归调用
            for iter_idx in range(start_idx, len_grid):
                # 先寻找从start_idx开始的下一个可以放新皇后的格子
                if grid_state[iter_idx] is 0:
                    continue
                # 在这个格子放入皇后
                chess_board[iter_idx] = 'Q'
                # grid_state[iter_idx] = 0
                # 将新皇后势力范围内的格子（grid_state）都设置为0，此处可以选择两种check的方法
                # store_list = self.state_check(iter_idx, grid_state, n)
                store_list = self.state_check_new(iter_idx, grid_state, n)

                self.search_answer(grid_state, res_n-1, iter_idx+1, result_list, chess_board, len_grid, n)
                # 函数返回前，要把因为放置这个皇后而更改过的grid_state和chess_board复原
                chess_board[iter_idx] = '.'
                for idx in store_list:
                    grid_state[idx] = 1
            return None

    # 复杂度为o(n**2)的格子判断方法，不够优化
    def state_check(self, idx, grid_state, n):
        # 行的判断标准
        # 在棋盘上放入一个新的皇后，然后将和这个皇后处在同一行的格子状态都设置为0
        # 皇后的位置在idx，那么这一行的索引号就是从n*(idx // n)， 到n*(idx // n+1)-1
        row_list = list(range(n*(idx//n), n*(idx//n+1)))

        # 列的判断标准
        # 在棋盘上放入一个新的皇后，然后将和这个皇后处在同一列的格子状态都设置为0
        # 皇后的位置在idx，那么这一行的索引号就是range(idx%n, n**2, n)
        col_list = list(range(idx%n, n**2, n))

        # 斜线的判断标准
        # 在棋盘上放入一个新的皇后，然后将和这个皇后处在相同的两条斜线上的格子状态都设置为0
        # 先计算每个格子的row_idx和col_idx
        # 每个皇后都有两条斜线，其中一条斜线上的格子row_idx+col_idx和皇后的相同
        # 另外一条斜线的row_idx-col_idx和皇后的相同
        queen_row_idx = idx//n
        queen_col_idx = idx%n
        queen_sum = queen_row_idx + queen_col_idx
        queen_sub = queen_row_idx - queen_col_idx

        # 进行判断，并且把因为放置这个皇后而导致不可用的格子都记录下来
        store_list = []
        for grid_idx in range(0, n**2):
            if grid_state[grid_idx] != 0:
                # 只对可用的格子进行检查，不可用的格子就跳过
                if grid_idx in (row_list+col_list):
                    # 检查行和列
                    grid_state[grid_idx] = 0
                    if grid_idx not in store_list:
                        store_list.append(grid_idx)

            if grid_state[grid_idx] != 0:
                # 检查两条斜线
                tmp_row_idx = grid_idx//n
                tmp_col_idx = grid_idx%n
                if (tmp_row_idx+tmp_col_idx) == queen_sum or (tmp_row_idx-tmp_col_idx) == queen_sub:
                    grid_state[grid_idx] = 0
                    if grid_idx not in store_list:
                        store_list.append(grid_idx)

        return store_list

    # 复杂度为o(n)的格子判断方法,比上一种方法好，但仍然通不过leetcode的时间测试
    def state_check_new(self, idx, grid_state, n):

        # 进行判断，并且把因为放置这个皇后而导致不可用的格子都记录下来
        store_list = []

        # 行的判断标准
        # 在棋盘上放入一个新的皇后，然后将和这个皇后处在同一行的格子状态都设置为0
        # 皇后的位置在idx，那么这一行的索引号就是从n*(idx // n)， 到n*(idx // n+1)-1

        # 将涉及到的行都将grid_state降为0:
        for grid_idx in range(n * (idx // n), n * (idx // n + 1)):
            if grid_state[grid_idx] != 0:
                grid_state[grid_idx] = 0
                store_list.append(grid_idx)

        # 列的判断标准
        # 在棋盘上放入一个新的皇后，然后将和这个皇后处在同一列的格子状态都设置为0
        # 皇后的位置在idx，那么这一行的索引号就是range(idx%n, n**2, n)
        # col_list = list(range(idx % n, n ** 2, n))
        for grid_idx in range(idx % n, n ** 2, n):
            if grid_state[grid_idx] != 0:
                grid_state[grid_idx] = 0
                store_list.append(grid_idx)

        # 斜线的判断标准
        # 在棋盘上放入一个新的皇后，然后将和这个皇后处在相同的两条斜线上的格子状态都设置为0
        # 先计算每个格子的row_idx和col_idx
        # 每个皇后都有两条斜线，其中一条斜线上的格子row_idx+col_idx和皇后的相同
        # 另外一条斜线的row_idx-col_idx和皇后的相同
        queen_row_idx = idx // n
        queen_col_idx = idx % n
        queen_sum = queen_row_idx + queen_col_idx
        queen_sub = queen_row_idx - queen_col_idx

        sum_list_row = list(range(min(queen_sum, n-1), max(queen_sum-n+1, 0)-1, -1))
        sum_list_col = list(range(max(0, queen_sum-n+1), min(queen_sum, n-1)+1))
        sum_list = [sum_list_row[idx]*n+sum_list_col[idx] for idx in range(0, len(sum_list_col))]

        if queen_sub >= 0:
            sub_list_row = list(range(queen_sub, n))
            sub_list_col = list(range(0, n-queen_sub))
            sub_list = [sub_list_row[idx] * n + sub_list_col[idx] for idx in range(0, len(sub_list_col))]
        else:
            sub_list_row = list(range(0, n+queen_sub))
            sub_list_col = list(range(-queen_sub, n))
            sub_list = [sub_list_row[idx] * n + sub_list_col[idx] for idx in range(0, len(sub_list_col))]

        for grid_idx in (sum_list+sub_list):
            if grid_state[grid_idx] != 0:
                grid_state[grid_idx] = 0
                store_list.append(grid_idx)

        return store_list


if __name__ == '__main__':
    n = 6
    my_test = Solution()
    start = time.time()
    return_list = my_test.solveNQueens(n)
    end = time.time()
    print(end-start)
    print(return_list)

