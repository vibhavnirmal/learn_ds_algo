// 1480. Running Sum of 1d Array

#include <iostream>
#include <vector>

std::vector<int> runningSum(std::vector<int> &nums)
{
    std::vector<int> sum;
    sum.push_back(nums[0]);
    for (auto i = 1; i < nums.size(); i++)
    {
        sum.push_back(sum[i - 1] + nums[i]);
    }
    return sum;
}

int main(){
    std::vector<int> nums = {1,2,3,4};
    std::vector<int> result;

    result = runningSum(nums);

    for (auto i:result){
        std::cout<<i<<" ";
    }
    
}