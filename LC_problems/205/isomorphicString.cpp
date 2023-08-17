// 205. Isomorphic Strings
// https://leetcode.com/problems/isomorphic-strings

#include <iostream>
#include <string>
#include <unordered_map>

bool isIsomorphic(std::string s, std::string t)
{
    std::unordered_map<char, char> m;
    std::unordered_map<char, char> m2;

    for (int i = 0; i < s.size(); i++)
    {
        if (m.find(s[i]) == m.end())
            m[s[i]] = t[i];
        else if (m[s[i]] != t[i])
            return false;
    }

    for (int i = 0; i < t.size(); i++)
    {
        if (m2.find(t[i]) == m2.end())
            m2[t[i]] = s[i];
        else if (m2[t[i]] != s[i])
            return false;
    }

    return true;
}

int main()
{
    std::string s = "badc";
    std::string t = "baba";

    bool isIso;

    isIso = isIsomorphic(s, t);

    if (isIso)
        std::cout << "These strings are Isomorphic";
    else
        std::cout << "These strings are not Isomorphic";
}