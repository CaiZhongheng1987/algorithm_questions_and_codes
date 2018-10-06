# 编写一个程序，通过已填充的空格来解决数独问题。
#
# 一个数独的解法需遵循如下规则：
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
# 空白格用 '.' 表示。
#
#
# Note:
#
# 给定的数独序列只包含数字 1-9 和字符 '.' 。
# 你可以假设给定的数独只有唯一解。
# 给定数独永远是 9x9 形式的。
import time


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 首先遍历一遍数独，把每个空格可以填入的数字都保存下来
        rows_list = dict()
        cols_list = dict()
        rect_list = dict()
        judge_dict = dict()
        # 首先把已经有的数字都放入对应的字典中，用字符串拼接的形式，方便后面查找
        for row_idx in range(9):
            for col_idx in range(9):
                if board[row_idx][col_idx] != '.':
                    if row_idx not in rows_list:
                        rows_list[row_idx] = board[row_idx][col_idx]
                    else:
                        rows_list[row_idx] += board[row_idx][col_idx]
                    if col_idx not in cols_list:
                        cols_list[col_idx] = board[row_idx][col_idx]
                    else:
                        cols_list[col_idx] += board[row_idx][col_idx]
                    if (row_idx // 3, col_idx // 3) not in rect_list:
                        rect_list[row_idx // 3, col_idx // 3] = board[row_idx][col_idx]
                    else:
                        rect_list[row_idx // 3, col_idx // 3] += board[row_idx][col_idx]
                else:
                    if row_idx not in rows_list:
                        rows_list[row_idx] = ''
                    if col_idx not in cols_list:
                        cols_list[col_idx] = ''
                    if (row_idx // 3, col_idx // 3) not in rect_list:
                        rect_list[row_idx // 3, col_idx // 3] = ''

        # 然后再遍历一次，新建一个字典，用来存放每个格子可以选择的有效数字
        for row_idx in range(9):
            for col_idx in range(9):
                if board[row_idx][col_idx] == '.':
                    judge_dict[row_idx, col_idx] = [n for n in '123456789' if n not in (rows_list[row_idx] + cols_list[col_idx] + rect_list[row_idx // 3, col_idx // 3])]

        # 开始遍历，往里面填充新的数字，采用递归的方式
        _ = self.search_answer(board, judge_dict, False)
        return None

    def identify(self, str_num, row_idx, col_idx, store_dict, judge_dict, board):
        # 添加到board里面
        board[row_idx][col_idx] = str_num
        # 然后再judge_dict里面将该位置的key删掉，表明这个位置已经固定
        judge_dict.pop((row_idx, col_idx))
        # 然后删去有关联因素的行、列、小方块的judge_dict里面的相关value值。
        for r, c in judge_dict:
            if (r == row_idx or c == col_idx or (row_idx // 3, col_idx // 3) == (r // 3, c // 3)) and str_num in \
                    judge_dict[r, c]:
                # 删除之前先保存到store_dict里面
                store_dict[r, c] = str_num
                # 删除相关联的judge_dict
                judge_dict[r, c].remove(str_num)
                if len(judge_dict[r, c]) == 0:
                    return False
        return True

    def rollback_data(self, row_idx, col_idx, store_dict, judge_dict, board):
        # 说明这次尝试不对，于是恢复judge_dict和board
        board[row_idx][col_idx] = '.'
        for key in store_dict:
            if key in judge_dict:
                judge_dict[key].extend(store_dict[key])
            else:
                judge_dict[key] = store_dict[key]
        return None

    def search_answer(self, board, judge_dict, return_flag):
        if len(judge_dict) == 0:
            # 说明judge_dict已经用完，数独已经解出，可以返回了
            return True
        # 寻找长度最短的judge_dict
        (row_idx, col_idx) = min(judge_dict, key=lambda x: len(judge_dict[x]))
        for str_num in judge_dict[row_idx, col_idx]:
            # 将这个位置的judge_dict的可选值单独存一个字典store_dict
            store_dict = {(row_idx, col_idx): judge_dict[row_idx, col_idx]}
            tmp_return_flag = self.identify(str_num, row_idx, col_idx, store_dict, judge_dict, board)
            if tmp_return_flag is True:
                # 完成之后递归调用函数，进行下一步
                return_flag = self.search_answer(board, judge_dict, return_flag)
                if return_flag is True:
                    return return_flag

            # 回退judge_dict和board
            self.rollback_data(row_idx, col_idx, store_dict, judge_dict, board)

        return False


# main test script
# test_list = [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]

test_list = [
    [".",".","9","7","4","8",".",".","."],
    ["7",".",".",".",".",".",".",".","."],
    [".","2",".","1",".","9",".",".","."],
    [".",".","7",".",".",".","2","4","."],
    [".","6","4",".","1",".","5","9","."],
    [".","9","8",".",".",".","3",".","."],
    [".",".",".","8",".","3",".","2","."],
    [".",".",".",".",".",".",".",".","6"],
    [".",".",".","2","7","5","9",".","."]
]

# test_list = [
#     ["5","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]
# ]

# test_list = [
#     [".",".","9","7","4","8",".",".","."],
#     ["7",".",".",".",".",".",".",".","."],
#     [".","2",".","1",".","9",".",".","."],
#     [".",".","7",".",".",".","2","4","."],
#     [".","6","4",".","1",".","5","9","."],
#     [".","9","8",".",".",".","3",".","."],
#     [".",".",".","8",".","3",".","2","."],
#     [".",".",".",".",".",".",".",".","6"],
#     [".",".",".","2","7","5","9",".","."]
# ]

my_test = Solution()
start = time.time()
my_test.solveSudoku(test_list)
end = time.time()
print(end-start)
for idx in range(9):
    print(test_list[idx])
