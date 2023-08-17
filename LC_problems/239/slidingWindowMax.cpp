#include <iostream>
#include <vector>
#include <deque>

std::vector<int> maxSlidingWindow(std::vector<int>& nums, int k) {
    std::vector<int> result;
    if (k == 0) return result;

    std::deque<int> w;
    
    for (int i = 0, n = (int)nums.size(); i < n; i++) {

        while (!w.empty() && w.front() <= i-k) 
            w.pop_front();

        while (!w.empty() && nums[w.back()] <= nums[i]) 
            w.pop_back();

        w.push_back(i);
        
        if (i >= k-1)
            result.push_back(nums[w.front()]);

    }
    return result;
}

int main(){
    std::vector<int> nums = {7,2,4};
    int k = 2;

    std::vector<int> result = maxSlidingWindow(nums, k);
    for (int i = 0; i < result.size(); i++){
        std::cout << result[i] << " ";
    }

    std::cout << std::endl;
    return 0;
}