# 算法题目和代码

说明：这些题目都是从leetcode或者其余的算法书上看到的，基本上别人都已有最优解答，我这里只是出于自己学习的需要，重新用python练习一遍，搞懂每个步骤。

## 001. 用递归函数和栈操作逆序一个栈
说明：一个栈依次压入1、2、3、4、5，那么从栈顶到栈底分别为5、4、3、2、1。将这个栈转置后，从栈顶到栈底为1、2、3、4、5，也就是实现栈中元素的逆序，但是只能用递归函数来实现，不能用其他数据结构。

代码：https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/tree/master/001

## leetcode001.两数之和
说明：给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

代码：https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode001/test_two_sum.py

## leetcode002.两数相加
说明：定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

代码：https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode002/test_Add_Two_Numbers_leetcode.py

## leetcode003.无重复字符的最长子串
说明：给定一个字符串，找出不含有重复字符的最长子串的长度。

示例：

给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。

给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。

给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。

代码：https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode003/test_Longest_Substring_Without_Repeating_Characters.py

## leetcode004.两个排序数组的中位数
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。

请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。

你可以假设 nums1 和 nums2 不同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

中位数是 (2 + 3)/2 = 2.5

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode004/test_Median_of_Two_Sorted_Arrays.py

## leetcode005.最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode005/test_Longest_Palindromic_Substring.py

## leetcode006.Z字形变换
将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：

P　　  A 　　 H 　　 N

A　P　L　S　I　I　G

Y　 　 I　　  R

之后从左往右，逐行读取字符："PAHNAPLSIIGYIR"

实现一个将字符串进行指定行数变换的函数:

string convert(string s, int numRows);
示例 1:

输入: s = "PAYPALISHIRING", numRows = 3
输出: "PAHNAPLSIIGYIR"
示例 2:

输入: s = "PAYPALISHIRING", numRows = 4
输出: "PINALSIGYAHRPI"
解释:

P     I    N

A   L S  I G

Y A   H R

P     I


代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode006/test_ZigZag_Conversion.py


## leetcode007.反转整数
给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode007/test_Reverse_Integer.py


## leetcode015.三数之和
说明：给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

代码：https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode015/test_three_sum.py
