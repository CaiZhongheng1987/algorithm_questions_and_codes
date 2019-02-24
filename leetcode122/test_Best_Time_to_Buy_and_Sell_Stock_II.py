# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

# 示例 1:
# 输入: [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
#
# 示例 2:
# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#
# 示例 3:
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # 使用贪心算法，从一个点开始，判断价格是否递增，如果递增就一直持有，如果价格下降了，就卖出。
        # 这样可以在o(n)复杂度内完成贪心算法
        if not prices:
            return 0
        len_prices = len(prices)
        if len_prices is 1:
            return 0
        cur_profit = 0
        buy_idx = 0  # 0: buy, 1: sell
        for idx in range(len_prices-2):
            if prices[idx+1] < prices[idx]:
                # 卖出
                cur_profit += prices[idx]-prices[buy_idx]
                # 下一次买入
                buy_idx = idx+1
        # 到此时我们已经走到倒数第二个价格
        if prices[-1] > prices[-2]:
            cur_profit += prices[-1] - prices[buy_idx]
        else:
            cur_profit += prices[-2] - prices[buy_idx]

        return cur_profit


if __name__ == '__main__':
    input_array = [7,6,4,3,1]
    my_test = Solution()
    return_profit = my_test.maxProfit(input_array)
    print(return_profit)
