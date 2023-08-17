#include <iostream>
#include <vector>

std::vector<int> twoSum(std::vector<int>& nums, int target) {
    for(int i=0; i<nums.size(); i++){
        for(int j=i+1; j<nums.size(); j++){
            if ((nums[i]+nums[j])==target){
                return {i, j};
            }
        }
    }
    return {};
}

int main(){
    std::vector<int> nums = {2,7,11,15};
    int target = 9;

    std::vector<int> result = twoSum(nums, target);

    std::cout<<"The values that make up the target is:"<<std::endl;

    for(auto i:result){
        std::cout<<i<<" ";
    }
}