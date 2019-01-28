# 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
#
# 示例:
#
# 输入: 3
# 输出:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        # 创建初始矩阵
        return_matrix = [[0]*n for _ in range(n)]

        # 先标记矩阵的四个角
        left_top = [0, 0]
        left_bottom = [n-1, 0]
        right_top = [0, n-1]
        right_bottom = [n-1, n-1]
        iter_num = 0
        in_list = list(range(1, n**2+1))

        while in_list:
            if iter_num is 0:
                # 行模式，填满matrix的第一行，正序
                for idx in range(left_top[1], right_top[1]+1):
                    return_matrix[left_top[0]][idx] = in_list.pop(0)
                left_top[0] += 1
                right_top[0] += 1
            elif iter_num is 1:
                # 列模式，填满matrix的最后一列，正序
                for idx in range(right_top[0], right_bottom[0]+1):
                    return_matrix[idx][right_top[1]] = in_list.pop(0)
                right_top[1] -= 1
                right_bottom[1] -= 1
            elif iter_num is 2:
                # 行模式，取出matrix的最后一行，倒序
                for idx in range(right_bottom[1], left_bottom[1]-1, -1):
                    return_matrix[right_bottom[0]][idx] = in_list.pop(0)
                right_bottom[0] -= 1
                left_bottom[0] -= 1
            else:
                # 列模式，填满matrix的第一列，倒序
                for idx in range(left_bottom[0], left_top[0]-1, -1):
                    return_matrix[idx][left_top[1]] = in_list.pop(0)
                left_bottom[1] += 1
                left_top[1] += 1

            iter_num = (iter_num+1) % 4
        return return_matrix


if __name__ == '__main__':
    input_num = 6
    my_test = Solution()
    out_list = my_test.generateMatrix(input_num)
    for line_idx in range(input_num):
        print(out_list[line_idx])
