// 344. Reverse String
// https://leetcode.com/problems/reverse-string/description/

// Write a function that reverses a string. 

// If stored in array/vector
    // You must do this by modifying the input array in-place with O(1) extra memory.

// g++ -o stringReverse rev_string.cpp


#include <iostream>
#include <string>

void twoPointerApproach(std::string myStr){
    int left = 0;
    int right = myStr.size() -1;

    while (left < right){
        std::swap(myStr[left], myStr[right]);
        left++;
        right--;
    }

    std::cout<< myStr;
}

int main(){
    std::string mystring;
    std::cout<<"Enter String to reverse:"<<std::endl;
    std::cin>> mystring;

    for(int i=mystring.size();i>=0;i--){
        std::cout<<mystring[i];
    }

    std::cout<<std::endl;

    twoPointerApproach(mystring);
}