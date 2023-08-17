// g++ -std=c++17 -o anagram .\anagram.cpp
// https://leetcode.com/problems/valid-anagram
// 242. Valid Anagram

// unordered map (hash map) to count the character frequency and check with target string is it matches
// O(n) space complexity

// or sort both strings and compare (sometimes in O(1) space complexity not everytime..)
// sorting takes nlogn time complexity

// it does not handle input strings with spaces or special characters 

// To remove non-alphabetic characters from both strings
    // s.erase(std::remove_if(s.begin(), s.end(), [](char c) { return !std::isalpha(c); }), s.end());
    // t.erase(std::remove_if(t.begin(), t.end(), [](char c) { return !std::isalpha(c); }), t.end());

#include <iostream>
#include <string>
#include <unordered_map>

bool isAnagram(std::string s, std::string t)
{
    std::unordered_map<char, int> freq;

    if (s.size() != t.size())
        return false;

    for (auto i : s)
        freq[i]++;

    for (auto j : t)
        freq[j]--;

    for (const auto &[key, val] : freq)
        if (val != 0)
            return false;

    return true;
}

int main()
{
    std::string s, t;

    std::cout << "Enter string s:" << std::endl;
    std::cin >> s;

    std::cout << "Enter string t:" << std::endl;
    std::cin >> t;

    bool anag;

    anag = isAnagram(s, t);

    if (anag)
        std::cout << "Is Anagram";
    else
        std::cout << "Is not Anagram";

    return 0;
}
