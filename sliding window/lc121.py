def maxProfit(prices):
    min_num = prices[0]
    ans = 0
    for i in prices:
        min_num = min(i, min_num)
        ans = max(ans, i-min_num)
    return ans

print(maxProfit(prices = [7,1,5,3,6,4]))