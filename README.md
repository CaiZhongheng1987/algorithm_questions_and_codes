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

## leetcode008.字符串转整数
实现 atoi，将字符串转为整数。

在找到第一个非空字符之前，需要移除掉字符串中的空格字符。如果第一个非空字符是正号或负号，选取该符号，并将其与后面尽可能多的连续的数字组合起来，这部分字符即为整数的值。如果第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

字符串可以在形成整数的字符后面包括多余的字符，这些字符可以被忽略，它们对于函数没有影响。

当字符串中的第一个非空字符序列不是个有效的整数；或字符串为空；或字符串仅包含空白字符时，则不进行转换。

若函数不能执行有效的转换，返回 0。

说明：

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。如果数值超过可表示的范围，则返回  INT_MAX (2^31 − 1) 或 INT_MIN (−2^31) 。

示例 1:

输入: "42"

输出: 42

示例 2:

输入: "   -42"

输出: -42

解释: 第一个非空白字符为 '-', 它是一个负号。我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。

示例 3:

输入: "4193 with words"

输出: 4193

解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。

示例 4:

输入: "words and 987"

输出: 0

解释: 第一个非空字符是 'w', 但它不是数字或正、负号。因此无法执行有效的转换。

示例 5:

输入: "-91283472332"

输出: -2147483648

解释: 数字 "-91283472332" 超过 32 位有符号整数范围。因此返回 INT_MIN (−2^31) 。

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode008/test_String_to_Integer.py

## leetcode009.回文数
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121

输出: true

示例 2:

输入: -121

输出: false

解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:

输入: 10

输出: false

解释: 从右向左读, 为 01 。因此它不是一个回文数。

进阶:

你能不将整数转为字符串来解决这个问题吗？

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode009/test_Palindrome_Number.py

## leetcode010.正则表达式匹配

给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的元素。
匹配应该覆盖整个字符串 (s) ，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: '*' 代表可匹配零个或多个前面的元素, 即可以匹配 'a' 。因此, 重复 'a' 一次, 字符串可变为 "aa"。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个('*')任意字符('.')。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 'c' 可以不被重复, 'a' 可以被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false

代码：

1、递归函数
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode010/test_Regular_Expression_Matching.py

2、动态规划实现
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode010/test_Regular_Expression_Matching_dp.py

## leetcode011.盛最多水的容器
给定n个非负整数a1，a2，...，an，每个数代表坐标中的一个点(i, ai) 。在坐标内画n条垂直线，垂直线i的两个端点分别为(i, ai)和(i, 0)。找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且n的值至少为2。

图中垂直线代表输入数组[1, 8, 6, 2, 5, 4, 8, 3, 7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为49。

示例:

输入: [1, 8, 6, 2, 5, 4, 8, 3, 7]

输出: 49

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode011/test_Container_With_Most_Water.py

## leetcode012. 整数转罗马数字
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

示例 1:

输入: 3
输出: "III"
示例 2:

输入: 4
输出: "IV"
示例 3:

输入: 9
输出: "IX"
示例 4:

输入: 58
输出: "LVIII"
解释: C = 100, L = 50, XXX = 30, III = 3.
示例 5:

输入: 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode012/test_Integer_to_Roman.py

## leetcode013.罗马数字转整数
罗马数字包含以下七种字符：I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

示例 1:

输入: "III"
输出: 3
示例 2:

输入: "IV"
输出: 4
示例 3:

输入: "IX"
输出: 9
示例 4:

输入: "LVIII"
输出: 58
解释: C = 100, L = 50, XXX = 30, III = 3.
示例 5:

输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode013/test_Roman_to_Integer.py


## leetcode014.最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode014/test_Longest_Common_Prefix.py

## leetcode015.三数之和
说明：给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode015/test_three_sum.py

## leetcode016.最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode016/test_3Sum%20Closest.py

## leetcode017.电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。


示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode017/test_Letter_Combinations_of_a_Phone_Number.py

## leetcode018.四数之和
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：

[
  [-1,  0, 0, 1],
  
  [-2, -1, 1, 2],
  
  [-2,  0, 0, 2]
  
]

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode018/test_4Sum.py

## leetcode019.删除链表的倒数第N个节点
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode019/test_Remove_Nth_Node_From_End_of_List.py

## leetcode020.有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode020/test_Valid_Parentheses.py

## leetcode021.合并两个有序链表
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4

输出：1->1->2->3->4->4

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode021/test_Merge_Two_Sorted_Lists.py

## leetcode022.括号生成
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode022/test_Generate_Parentheses.py

## leetcode023.合并K个排序链表
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  
  1->3->4,
  
  2->6
]

输出: 1->1->2->3->4->4->5->6

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode023/test_Merge_k_Sorted_Lists.py

## leetcode024.两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

说明:

你的算法只能使用常数的额外空间。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode024/test_Swap_Nodes_in_Pairs.py

## leetcode025.k个一组翻转链表
给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode025/test_Reverse_Nodes_in_k_Group.py

## leetcode026.删除排序数组中的重复项
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode026/test_Remove_Duplicates_from_Sorted_Array.py

## leetcode027.移除元素
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:

给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,1,2,2,3,0,4,2], val = 2,

函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

注意这五个元素可为任意顺序。

你不需要考虑数组中超出新长度后面的元素。

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode027/test_Remove_Element.py

## leetcode028.实现strStr()
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"

输出: 2

示例 2:

输入: haystack = "aaaaa", needle = "bba"

输出: -1

说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode028/test_Implement_strStr.py

## leetcode029.两数相除
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3

输出: 3

示例 2:

输入: dividend = 7, divisor = -3

输出: -2

说明:

被除数和除数均为 32 位有符号整数。

除数不为 0。

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode029/test_Divide_Two_Integers.py

## leetcode030.与所有单词相关联的字串
给定一个字符串 s 和一些长度相同的单词 words。在 s 中找出可以恰好串联 words 中所有单词的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

示例 1:

输入:
  s = "barfoothefoobarman",
  
  words = ["foo","bar"]
  
输出: [0,9]

解释: 从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。

输出的顺序不重要, [9,0] 也是有效答案。

示例 2:

输入:
  s = "wordgoodstudentgoodword",
  
  words = ["word","student"]
  
输出: []

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode030/test_Substring_with_Concatenation_of_All_Words.py

## leetcode031.下一个排列
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。

1,2,3 → 1,3,2

3,2,1 → 1,2,3

1,1,5 → 1,5,1

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode031/test_Next_Permutation.py

## leetcode032.最长有效括号
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"

输出: 2

解释: 最长有效括号子串为 "()"

示例 2:

输入: ")()())"

输出: 4

解释: 最长有效括号子串为 "()()"

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode032/test_Longest_Valid_Parentheses.py

## leetcode033.搜索旋转排序数组
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0

输出: 4

示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3

输出: -1

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode033/test_Search_in_Rotated_Sorted_Array.py

## leetcode034.在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8

输出: [3,4]

示例 2:

输入: nums = [5,7,7,8,8,10], target = 6

输出: [-1,-1]

代码：
https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode034/test_Find_First_and_Last_Position_of_Element_in_Sorted_Array.py
