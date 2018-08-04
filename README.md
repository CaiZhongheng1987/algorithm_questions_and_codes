# 算法题目和代码

说明：这些题目都是从leetcode或者其余的算法书上看到的，基本上别人都已有最优解答，我这里只是出于自己学习的需要，重新用python练习一遍，搞懂每个步骤。

## 001. 用递归函数和栈操作逆序一个栈
说明：一个栈依次压入1、2、3、4、5，那么从栈顶到栈底分别为5、4、3、2、1。将这个栈转置后，从栈顶到栈底为1、2、3、4、5，也就是实现栈中元素的逆序，但是只能用递归函数来实现，不能用其他数据结构。

代码：https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/tree/master/001

## leetcode001.两数之和
说明：给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

代码：https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode001/test_two_sum.py

## leetcode002.两数相加
给说明：定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

代码：https://github.com/CaiZhongheng1987/algorithm_questions_and_codes/blob/master/leetcode002/test_Add_Two_Numbers_leetcode.py

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
