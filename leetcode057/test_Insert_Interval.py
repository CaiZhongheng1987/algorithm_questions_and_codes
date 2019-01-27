# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
#
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
#
# 示例 1:
#
# 输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出: [[1,5],[6,9]]
# 示例 2:
#
# 输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出: [[1,2],[3,10],[12,16]]
# 解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            intervals.append(newInterval)
            return intervals

        len_list = len(intervals)
        for idx, val in enumerate(intervals):
            if val.end < newInterval.start:
                # val        :    -------
                # newInterval:             -------
                if idx is len_list-1:
                    intervals.append(newInterval)
                continue
            elif val.start <= newInterval.start <= val.end < newInterval.end:
                # val        :    -------
                # newInterval:         -------
                val.end = newInterval.end
                # 接下来就是leetcode56题的情况，合并重叠区间即可
                return self.merge(intervals[:idx], intervals[idx:])
            elif val.start > newInterval.start and val.end <= newInterval.end:
                # val        :    -------
                # newInterval:  -------------
                val.start = newInterval.start
                val.end = newInterval.end
                # 接下来就是leetcode56题的情况，合并重叠区间即可
                return self.merge(intervals[:idx], intervals[idx:])
            elif newInterval.start < val.start <= newInterval.end:
                # val        :            -------
                # newInterval:  -------------
                val.start = newInterval.start
                return intervals
            elif val.start > newInterval.end:
                # val        :                 -------
                # newInterval:  -------------
                intervals.insert(idx, newInterval)
                return intervals
            elif val.start <= newInterval.start and val.end >= newInterval.end:
                # val        :  ------------------
                # newInterval:     ----------
                return intervals
            else:
                pass

        return intervals

    def merge(self, result, intervals):
        # result = []
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
    # input_list = [[1,3],[2,6],[8,10],[15,18]]
    input_list = [[1, 5]]
    inter_list = []
    for val in input_list:
        tmp_inter = Interval(val[0], val[1])
        inter_list.append(tmp_inter)

    my_test = Solution()
    new_list = Interval(0, 0)
    return_list = my_test.insert(inter_list, new_list)
    print(return_list)
