# 121. Best Time to Buy and Sell Stock
# Easy

# 2 pointers

def maxProfit(prices):
    left, right = 0, 0
    maxP = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxP = max(maxP, profit)
        else:
            left = right
        right+=1
    return maxP

if __name__=="__main__":
    print(maxProfit(prices = [7,1,5,3,6,4]))
    print(maxProfit(prices = [7,6,4,3,1]))
