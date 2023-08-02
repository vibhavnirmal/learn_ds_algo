# 714. Best Time to Buy and Sell Stock with Transaction Fee
# Medium

# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8

# Input: prices = [1,3,7,5,10,3], fee = 3
# Output: 6

def maxProfit(prices, fee):
    profit = 0
    effectiveBP = prices[0]

    for i in range(len(prices)):
        profit = max(profit, prices[i] - effectiveBP - fee)
        effectiveBP = min(effectiveBP, prices[i] - profit)

    return profit

if __name__ == "__main__":
    print(maxProfit(prices = [1,3,2,8,4,9], fee = 2))
    print(maxProfit(prices = [1,3,7,5,10,3], fee = 3))
