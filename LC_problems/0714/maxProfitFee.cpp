// 714. Best Time to Buy and Sell Stock with Transaction Fee
// Medium

#include <iostream>
#include <vector>

int sellStocks(std::vector<int> prices, int fee){
    int maxProfit = 0;
    int minPrice = prices[0];

    for(auto price: prices){
        if(price < minPrice)
            minPrice = price;
        else if(price > minPrice + fee){
            maxProfit += price - minPrice - fee;
            minPrice = price - fee;
        }
    }

    return maxProfit;
}

int main(){
    std::vector<int> prices = {1,3,2,8,4,9};
    int fee = 2;

    prices = {1,3,7,5,10,3};
    fee = 3;

    int maxProfit;

    maxProfit = sellStocks(prices, fee);

    std::cout << maxProfit;


}