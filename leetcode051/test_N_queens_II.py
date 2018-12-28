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

        # 将棋盘用二维数组表示
        # 采用深度遍历搜索方式
        # 皇后一共有n个，这里用递归函数来实现
        result_list = []  # 建立解法的list
        chess_board = []
        for idx in range(n):
            row_board = ['.']*n
            chess_board.append(row_board)  # 建立棋盘二维数组，默认全用.来填充

        col_list = [0]*n  # 判断列上面有没有皇后，如果有，就将其改为1
        diag_135_list = [0]*(2*n-1)  # 判断135度的对角线上有没有皇后，如果有，就将其改为1
        diag_45_list = [0]*(2*n-1)  # 判断45度的对角线上有没有皇后，如果有，就将其改为1

        self.search_answer(0, result_list, chess_board, n, col_list, diag_135_list, diag_45_list)
        return result_list

    def search_answer(self, row_idx, result_list, chess_board, n, col_list, diag_135_list, diag_45_list):
        if row_idx == n:
            # 表明所有的n已经用完，且找到了正确的解答
            # return_flag = True
            # 记录下此时的chess_board
            tmp_result = []
            for idx in range(n):
                tmp_result.append(''.join(chess_board[idx]))

            result_list.append(tmp_result)
        else:
            # 在这一行扫描所有列
            for col_idx in range(n):
                # 判断这个点是否能够放入皇后，只需要判断列和对角线即可
                if col_list[col_idx] is 1:
                    # 说明这一列上有皇后
                    continue
                if diag_45_list[row_idx+col_idx] is 1:
                    # 说明45度对角线上有皇后
                    continue
                if diag_135_list[row_idx-col_idx+n-1] is 1:
                    # 说明135度对角线上有皇后，这里为了保证索引能被取到（因为索引值都是不小于0的），将row-col的差加上了n-1
                    continue
                # 到这一步说明当前的row_idx和col_idx可以放下一个皇后
                chess_board[row_idx][col_idx] = 'Q'
                col_list[col_idx] = 1
                diag_45_list[row_idx+col_idx] = 1
                diag_135_list[row_idx-col_idx+n-1] = 1
                # 递归调用，进入下一行继续扫描
                self.search_answer(row_idx+1, result_list, chess_board, n, col_list, diag_135_list, diag_45_list)
                # 进行复原
                chess_board[row_idx][col_idx] = '.'
                col_list[col_idx] = 0
                diag_45_list[row_idx + col_idx] = 0
                diag_135_list[row_idx - col_idx + n - 1] = 0
        return None


if __name__ == '__main__':
    n = 6
    my_test = Solution()
    start = time.time()
    return_list = my_test.solveNQueens(n)
    end = time.time()
    print(end-start)
    print(return_list)

