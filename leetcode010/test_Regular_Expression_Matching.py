# 给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符。
# '*' 匹配零个或多个前面的元素。
# 匹配应该覆盖整个字符串 (s) ，而不是部分字符串。
#
# 说明:
#
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
# 示例 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 示例 2:
#
# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: '*' 代表可匹配零个或多个前面的元素, 即可以匹配 'a' 。因此, 重复 'a' 一次, 字符串可变为 "aa"。
# 示例 3:
#
# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个('*')任意字符('.')。
# 示例 4:
#
# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 'c' 可以不被重复, 'a' 可以被重复一次。因此可以匹配字符串 "aab"。
# 示例 5:
#
# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false


# 采用递归函数来做字符串匹配
class Solution:
    def isMatch(self, s, p):
        len_p = len(p)
        len_s = len(s)

        if p == '':
            # p长度为0（空字符串）的情况，就要求s也必须为空字符串，否则就匹配失败
            return s == ''

        if len_p == 1:
            # p长度为1的情况
            # p要和s完全匹配，p就必须为.或者s[0]，且s的长度也为1
            # 备注：这里认为p长度为1的时候，p本身不能为*（因为*必须要前面存在一个字母或者.字符）
            # 所以*不能单独存在
            if len_s == 1 and (p in ['.', s[0]]):
                return True
            else:
                return False

        # 在这里，p长度大于1，s长度不定
        if p[1] != '*':
            # 首先看p[1]不为*的情况
            if s == '':
                # 如果p长度大于1，s是空字符串，那肯定不匹配
                return False
            elif p[0] in [s[0], '.']:
                # 如果p和s第一个字符相等或者p是任意字符.，且p的第二个字符不是*
                # 那就可以用递归函数，继续比较剩下的字符
                return self.isMatch(s[1:], p[1:])
            else:
                # 如果p和s的第一个字符就不相等了，那肯定不匹配
                return False
        else:
            # 如果p的第二个字符恰好就是*
            # *代表多个字符，那就需要一个个地将s往下进行比较。
            # 在比较过程中，s不能为空字符串，且p[0]一定要是.字符或者s[0]
            while s != '' and (p[0] in ['.', s[0]]):
                # 将p[2:]和s做匹配，递归调用函数，如果匹配成功，那就说明整个字符串都匹配成功
                # 这样做的原因是，s存在很多很长的相同字符，这里必须用while循环语句来把这些字符挤压掉
                # 如果匹配成功，这就说明s大概是'aaa', p是'a*a'这种形式
                # 当然，需要通过下面的s = s[1:]来不断去掉s中的a，最终匹配成功的是'a'和'a'
                return_val = self.isMatch(s, p[2:])
                if return_val is True:
                    return True
                else:
                    # 如果匹配不成功，那就说明重复的字符串还没去干净，就把s的第二个字符去掉
                    s = s[1:]

            # 到这一步，s已经为空字符串，还需要将s和p[2:]再做一次递归匹配，防止边界条件出问题
            # s是'aaa', p是'a*'这种形式
            # 或者s是'aaa', p是'c*a*'的形式
            return self.isMatch(s, p[2:])


s_string = 'ab'
p_string = ".*"

my_test = Solution()
result = my_test.isMatch(s_string, p_string)
print(result)
