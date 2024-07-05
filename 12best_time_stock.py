'''
Q: 한 번의 주식 거래로 낼 수 있는 최대 이익 산출하기

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

#time limit exeeded
class solution(object):
    def maxProfit(self, prices):
        maxp = 0
        
        for idx, item in enumerate(prices):
            for j in range(idx, len(prices)):
                maxp = max(prices[j]-item, maxp)

        return maxp

#solution
class solution2(object):
    def maxProfit(self, prices):
        profit = 0
        minp = 999999

        for price in prices:
            minp = min(minp, price)
            profit = max(profit, price - minp)
        return profit


