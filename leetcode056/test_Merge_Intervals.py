# 给出一个区间的集合，请合并所有重叠的区间。
#
# 示例 1:
#
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2:
#
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # 先对输入的list按照区间的起始点进行排序
        intervals.sort(key=lambda x: x.start)
        result = []
        for tmp_val in intervals:
            if not result or result[-1].end < tmp_val.start:
                # 如果已有列表的end都小于新加入的start，那就说明新加入一个不重叠的区间
                result.append(tmp_val)
            else:
                # 否则，就说明最后一个区间的end应该考虑扩展
                # 这里只考虑最后一个区间，是因为前面已经对interval进行了排序，
                # 新加入的区间，start只会比result[-1]的start大或者相等
                result[-1].end = max(result[-1].end, tmp_val.end)
        return result


if __name__ == '__main__':
    input_list = [[1,3],[2,6],[8,10],[15,18]]
    inter_list = []
    for val in input_list:
        tmp_inter = Interval(val[0], val[1])
        inter_list.append(tmp_inter)

    my_test = Solution()
    return_list = my_test.merge(inter_list)
    print(return_list)
