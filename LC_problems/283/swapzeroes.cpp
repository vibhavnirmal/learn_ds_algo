// 283. Move Zeroes
// Easy

#include <iostream>
#include <vector>

void moveZeroes(std::vector<int>& nums) { 
    int nonZeroCount = 0;
    for (int i=0; i<nums.size(); i++){
        if (nums[i] != 0){
            std::swap(nums[nonZeroCount++], nums[i]);
        }
    }
}

int main(){
    std::vector<int> nums = {0, 1, 0, 0, 0, 5};
    moveZeroes(nums);
    for (int i=0; i<nums.size(); i++){
        std::cout << nums[i] << " ";
    }
    std::cout << std::endl;
    return 0;
}