// 387. First Unique Character in a String
// https://leetcode.com/problems/first-unique-character-in-a-string

#include <iostream>
#include <unordered_map>
#include <string>

int main(){
    std::string s = "vibhav";
    std::unordered_map<char, int> m;

    for (auto i:s)
        m[i]++;
    for (auto i=0;i<s.size(); i++)
        if (m[s[i]] == 1){
            std::cout<<i;
            return 0;
        }
    std::cout<<"-1";
    return 0;
}