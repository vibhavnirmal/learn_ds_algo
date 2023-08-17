// https://leetcode.com/problems/find-pivot-index/
// 724. Find Pivot Index

#include <iostream>
#include <vector>

int pivotIndex(std::vector<int> nums) {
    int total, leftSum=0, rightSum;

    for (auto i:nums) {total += i;}
    for (auto i=0;i<nums.size();i++) {
        rightSum = total - nums[i] - leftSum;
        if (leftSum == rightSum){
            return i;
        }
        leftSum += nums[i];
    }
    return -1;
}

int main(){

    std::vector<int> myVector = {1,1,1,3,3};
    int idxVal;

    idxVal = pivotIndex(myVector);

    std::cout<<"Index is : "<<idxVal;
}