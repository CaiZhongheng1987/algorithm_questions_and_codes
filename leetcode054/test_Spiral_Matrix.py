# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#
# 示例 1:
#
# 输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 示例 2:
#
# 输入:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        iter_num = 0
        return_list = []

        while matrix:
            if iter_num is 0:
                # 行模式，取出matrix的第一行
                return_list.extend(matrix.pop(0))
            elif iter_num is 1:
                # 列模式，取出matrix的最后一列
                for iter_idx in range(len(matrix)):
                    return_list.append(matrix[iter_idx].pop(-1))
                # 到这一步容易出现[[],[]]的matrix，所以需要删掉
                while matrix and not matrix[0]:
                    del matrix[0]
            elif iter_num is 2:
                # 行模式，取出matrix的最后一行，倒序
                tmp_list = matrix.pop(-1)
                tmp_list.reverse()
                return_list.extend(tmp_list)
            else:
                # 列模式，取出matrix的第一列，倒序
                for iter_idx in range(len(matrix)-1, -1, -1):
                    return_list.append(matrix[iter_idx].pop(0))
                # 到这一步容易出现[[],[]]的matrix，所以需要删掉
                while matrix and not matrix[-1]:
                    del matrix[-1]

            iter_num = (iter_num+1) % 4

        return return_list


if __name__ == '__main__':
    input_list = [[7],[9],[6]]
    my_test = Solution()
    out_list = my_test.spiralOrder(input_list)
    print(out_list)
