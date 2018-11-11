# 给定一个 n × n 的二维矩阵表示一个图像。
#
# 将图像顺时针旋转 90 度。
#
# 说明：
#
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
#
# 示例 1:
#
# 给定 matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# 示例 2:
#
# 给定 matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 将矩阵看成回字形的结构，一层一层地往里面顺时针旋转90度。
        # 旋转过程中，额外开启一个元素的空间作为寄存的中间变量

        # 先计算回字形的结构有多少层，注意n为奇数的时候，最中间的元素不需要旋转
        len_matrix = len(matrix)
        layer_num = len_matrix // 2
        for layer_idx in range(layer_num):
            for iter_idx in range(layer_idx, len_matrix-layer_idx-1):
                # 每次旋转之前，将第一个数存入临时变量
                tmp_val = matrix[layer_idx][iter_idx]
                # 依次顺时针移动
                matrix[layer_idx][iter_idx] = matrix[len_matrix-iter_idx-1][layer_idx]
                matrix[len_matrix-iter_idx-1][layer_idx] = matrix[len_matrix-layer_idx-1][len_matrix-iter_idx-1]
                matrix[len_matrix-layer_idx-1][len_matrix-iter_idx-1] = matrix[iter_idx][len_matrix-layer_idx-1]
                matrix[iter_idx][len_matrix-layer_idx-1] = tmp_val

        return None


input_matrix = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]

my_test = Solution()
my_test.rotate(input_matrix)
print(input_matrix)
