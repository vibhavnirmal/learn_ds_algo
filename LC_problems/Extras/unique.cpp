// string has unique characters

#include <iostream>
#include <string>

int main()
{
    std::string s = "vibhav";

    for (int i = 0; i < s.size(); i++)
    {
        for (int j = i+1; j < s.size(); j++)
        {
            // std::cout<<s[i]<<" "<<s[j];
            if (s[i] == s[j])
            {
                std::cout << "Not unique";
                return 0;
            }
        }
    }

    std::cout<<"unique";
    return 0;
}

// #include <iostream>
// #include <string>
// #include <unordered_set>

// int main()
// {
//     std::string s = "vibhav";
//     std::unordered_set<char> seen;

//     for (char c : s){
//         if (seen.count(c) > 0){
//             std::cout << "Not unique";
//             return 0;
//         }
//         else
//             seen.insert(c);
//     }

//     std::cout << "unique";
//     return 0;
// }
