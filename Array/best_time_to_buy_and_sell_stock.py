class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_till_now=prices[0]
        max_profit=0
        today_profit=0
        for i in range(len(prices)):
            if min_till_now>prices[i]:
                min_till_now=prices[i]
            today_profit=prices[i]-min_till_now
            max_profit=max(today_profit,max_profit)
        return max_profit







# prices=[7,1,5,3,6,4]
# min_till_now=prices[0]
# max_profit=0
# today_profit=0
# for i in range(len(prices)):
#     if min_till_now>prices[i]:
#         min_till_now=prices[i]
#         # print(min_till_now)
#     today_profit=prices[i]-min_till_now
#     max_profit=max(today_profit,max_profit)
# print(max_profit)