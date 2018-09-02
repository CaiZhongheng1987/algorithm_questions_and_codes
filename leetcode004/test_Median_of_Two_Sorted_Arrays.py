# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
#
# 请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
#
# 你可以假设 nums1 和 nums2 不同时为空。
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 中位数是 2.0
#
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 中位数是 (2 + 3)/2 = 2.5
import copy


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        idx1 = 0
        idx2 = 0
        m = len(nums1)
        n = len(nums2)
        len_total = m + n

        # 先判断两个数组中是否有一个为空数组，如果有，直接取中位数然后返回
        if m == 0 or n == 0:
            nums1.extend(nums2)
            mid_num = Solution.find_single_array(self, nums1, len_total)
            return mid_num

        # 在两个数组都不为空的情况下，先将两个数组进行大致排序，确保nums1数组的第一个值是两个数组里面的最小值
        if nums2[idx2] < nums1[idx1]:
            nums2, nums1 = nums1, nums2
            n, m = m, n

        # 将两个数组分为三种情况进行讨论
        if nums2[0] < nums1[-1]:
            if nums2[-1] < nums1[-1]:
                # 第1种情况
                # ---------
                #     ---
                # find_case = 1
                lowest_idx = Solution.find_lowest_cross_idx(self, nums1, nums2[0], m)
                # 对lowest_idx进行处理，判断这个序号位于m+n的中心点左边还是右边
                if len_total % 2:
                    if lowest_idx >= int(len_total / 2):
                        # 说明nums1[0:lowest_idx]当中就能取出两个数组的中位数
                        mid_num = Solution.find_single_array(self, nums1, len_total)
                        return mid_num
                else:
                    if lowest_idx > int(len_total/2) - 1:
                        mid_num = Solution.find_single_array(self, nums1, len_total)
                        return mid_num
                    elif lowest_idx == int(len_total/2) - 1:
                        tmp_val = min(nums2[0], nums1[lowest_idx + 1])
                        return (tmp_val + nums1[lowest_idx]) / 2
                    else:
                        pass

                # 再计算上界，求得highest_idx.
                highest_idx = Solution.find_highest_cross_idx(self, nums1, nums2[-1], m)
                # 对highst_idx进行处理，判断这个序号位于m+n的中心点左边还是右边
                if (highest_idx+n) < int(len_total/2):
                    # 说明nums1[highest_idx:]当中就能取出两个数组的中位数，直接把两个数组拼接，当成一个数组来求中位数即可
                    nums2.extend(nums1)
                    mid_num = Solution.find_single_array(self, nums2, len_total)
                else:
                    # 到这一步，就说明中位数在两个数组的交叉区域
                    # 两个数组从开始到中位数之间的数必定都包含两个数组的数
                    mid_num = Solution.find_cross_idx(self, nums1, nums2, len_total)

                return mid_num
            else:
                # 第2种情况
                # ---------
                #      --------
                # find_case = 2
                lowest_idx = Solution.find_lowest_cross_idx(self, nums1, nums2[0], m)
                # 对lowest_idx进行处理，判断这个序号位于m+n的中心点左边还是右边
                if len_total % 2:
                    if lowest_idx >= int(len_total / 2):
                        # 说明nums1[0:lowest_idx]当中就能取出两个数组的中位数
                        mid_num = Solution.find_single_array(self, nums1, len_total)
                        return mid_num
                else:
                    if lowest_idx > int(len_total/2) - 1:
                        mid_num = Solution.find_single_array(self, nums1, len_total)
                        return mid_num
                    elif lowest_idx == int(len_total/2) - 1:
                        tmp_val = min(nums2[0], nums1[lowest_idx + 1])
                        return (tmp_val + nums1[lowest_idx]) / 2
                    else:
                        pass

                highest_idx = Solution.find_highest_cross_idx(self, nums2, nums1[-1], n)
                # 对highest_idx进行处理，判断这个序号位于m+n的中心点左边还是右边
                if (highest_idx+m) < int(len_total / 2):
                    # 说明nums2[highest_idx:]当中就能取出两个数组的中位数，直接把两个数组拼接，当成一个数组来求中位数即可
                    nums1.extend(nums2)
                    mid_num = Solution.find_single_array(self, nums1, len_total)
                else:
                    # 到这一步，就说明中位数在两个数组的交叉区域
                    # 两个数组从开始到中位数之间的数必定都包含两个数组的数
                    mid_num = Solution.find_cross_idx(self, nums1, nums2, len_total)

                return mid_num
        else:
            # 第3种情况，直接计算中位数
            # ---------
            #           --------
            # find_case = 3
            nums1.extend(nums2)
            mid_num = Solution.find_single_array(self, nums1, len_total)
            return mid_num

    # 子函数，针对一个不为空的有序数组，直接查找该数组的中位数
    def find_single_array(self, tmp_list, tmp_len):
        if tmp_len % 2:  # 数组长度是奇数
            tmp_mid_num = tmp_list[int(tmp_len / 2)]
        else:  # 数组长度是偶数
            tmp_mid_num = (tmp_list[int(tmp_len / 2)] + tmp_list[int(tmp_len / 2) - 1]) / 2

        return tmp_mid_num

    # 子函数，在第一和第三种情况下，寻找nums1在哪个idx和nums2相交，寻找下界，即下面的*号位置
    # -------*-----
    #         ---------
    def find_lowest_cross_idx(self, tmp_list1, final_num, m):
        right_idx = m - 1
        left_idx = 0
        mid_idx = int((left_idx + right_idx) / 2)
        flag1 = False

        while flag1 is False:
            flag1 = (tmp_list1[mid_idx] <= final_num) and (tmp_list1[mid_idx + 1] >= final_num)
            if flag1 is True:
                break

            if tmp_list1[mid_idx] > final_num:
                right_idx = mid_idx
            else:  # tmp_list1[mid_idx] < tmp_list2[0]:
                left_idx = mid_idx

            mid_idx = int((left_idx + right_idx) / 2)

        return mid_idx

        # 子函数，在第一种情况下，寻找nums1在哪个idx和nums2相交，寻找上界，即下面的*号位置
        # ---------*--
        #      ----
    def find_highest_cross_idx(self, tmp_list1, final_num, m):
        right_idx = m - 1
        left_idx = 0
        mid_idx = int((left_idx + right_idx) / 2)
        flag1 = False

        while flag1 is False:
            flag1 = (tmp_list1[mid_idx] >= final_num) and (tmp_list1[mid_idx - 1] <= final_num)
            if flag1 is True:
                break

            if tmp_list1[mid_idx] > final_num:
                right_idx = mid_idx
            else:  # tmp_list1[mid_idx] < final_num:
                if left_idx == mid_idx:
                    left_idx = right_idx  # 这是为了防止出现left为0，mid为1，right为2，但我们需要的又正好是2的情况
                else:
                    left_idx = mid_idx

            mid_idx = int((left_idx + right_idx) / 2)

        return mid_idx

    # 在两个数组的交叉区域寻找中位数
    def find_cross_idx(self, tmp_list1, tmp_list2, tmp_len_total):
        # 假设我们找到中位数后，list1的位置为idx1，list2的位置为idx2
        # 进入这个函数，就表示一定存在idx1和idx2，且
        return_flag = 0
        m = len(tmp_list1)
        n = len(tmp_list2)
        left_idx_2 = 0
        right_idx_2 = n - 1
        idx2 = int((n / 2)) #既然idx2一定存在，初始值就赋值为list2一半的位置
        idx1 = 0
        # 首先判断两个数组长度之和是偶数还是奇数
        if tmp_len_total % 2:  # 数组长度是奇数
            tmp_mid_idx = int(tmp_len_total / 2)
        else:
            tmp_mid_idx = int(tmp_len_total / 2) - 1

        while return_flag == 0:
            print(idx1, idx2)
            idx1 = tmp_mid_idx - idx2 - 1
            if idx1 < 0:
                right_idx_2 = idx2
                idx2 = int((left_idx_2 + right_idx_2) / 2)
                continue
            elif idx1 > m - 1:
                left_idx_2 = idx2
                idx2 = int((left_idx_2 + right_idx_2) / 2)
                if idx2 == left_idx_2:
                    idx2 = idx2 + 1
                continue
            else:
                if tmp_list1[idx1] > tmp_list2[idx2]:
                    if idx2 == n - 1:
                        if tmp_len_total % 2:  # 数组长度是奇数
                            return tmp_list1[idx1]
                        else:
                            return (tmp_list1[idx1 + 1] + tmp_list1[idx1]) / 2
                    else:
                        if tmp_list1[idx1] <= tmp_list2[idx2 + 1]:
                            break
                        else:
                            left_idx_2 = idx2
                            idx2 = int((left_idx_2 + right_idx_2) / 2)
                            if idx2 == left_idx_2:
                                idx2 = idx2 + 1
                elif tmp_list1[idx1] < tmp_list2[idx2]:
                    if idx1 == m - 1:
                        if tmp_len_total % 2:  # 数组长度是奇数
                            return tmp_list2[idx2]
                        else:
                            return (tmp_list2[idx2 + 1] + tmp_list2[idx2]) / 2
                    else:
                        if tmp_list1[idx1+1] >= tmp_list2[idx2]:
                            break
                        else:
                            right_idx_2 = idx2
                            idx2 = int((left_idx_2 + right_idx_2) / 2)

                else:  # 两者相等的情况，单独考虑
                    break

        if tmp_len_total % 2:
            return max(tmp_list2[idx2], tmp_list1[idx1])
        else:
            if idx1 == m - 1:
                return (tmp_list1[idx1] + tmp_list2[idx2 + 1]) / 2
            elif idx2 == n - 1:
                return (tmp_list1[idx1 + 1] + tmp_list2[idx2]) / 2
            else:
                tmp_val = min(tmp_list1[idx1 + 1], tmp_list2[idx2 + 1])
                if tmp_list1[idx1] > tmp_list2[idx2]:
                    return (tmp_list1[idx1] + tmp_val) / 2
                else:
                    return (tmp_list2[idx2] + tmp_val) / 2


# list1 = [1, 2, 3]
# list2 = [1, 2, 2]

# list1 = [1, 2]
# list2 = [3, 4]

# list1 = [6]
# list2 = [1, 2, 3, 4, 5, 7, 8]

#
# list1 = [1, 2, 3]
# list2 = [1, 2, 2]
#
# list1 = [1, 2]
# list2 = [1, 2]

# list1 = [1]
# list2 = [2, 3]

# list1 = [1, 3]
# list2 = [2, 4, 5, 6]

# list1 = [1, 3]
# list2 = [2]

# list1 = [2, 3]
# list2 = [1, 4, 5, 6, 7]

# list1 = [1, 2]
# list2 = [-1, 3]

# list1 = [3]
# list2 = [1, 2, 4]

list1 = [4, 6]
list2 = [1, 2, 3, 5]

new_list1 = copy.deepcopy(list1)
new_list2 = copy.deepcopy(list2)

my_test = Solution()
middle_num = my_test.findMedianSortedArrays(list1, list2)
print(middle_num)

# 构造比对脚本
new_list1.extend(new_list2)
new_list1.sort()
if len(new_list1) % 2:
    new_middle_num = new_list1[int(len(new_list1) / 2)]
else:
    new_middle_num = (new_list1[int(len(new_list1) / 2)] + new_list1[int(len(new_list1) / 2) - 1]) / 2

print(new_middle_num)
