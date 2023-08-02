// g++ -std=c++2a -fconcepts -o itr_algo 5_iter_algo.cpp && ./itr_algo

/*
    -> Iterators are objects that point to a specific element in a container
    -> Range-based for loops and their syntax using auto and auto&
    -> Type aliases using the "using" keyword
    -> Unordered map container and its basic functionality
    -> Structured bindings and how they can be used to extract values from a container during iteration
    -> Sorting an array using the std::sort() algorithm
    -> Searching an array using the std::binary_search() algorithm
*/

// reference: https://www.youtube.com/watch?v=SgcHcbQ0RCQ
// https://en.cppreference.com/w/cpp/container/unordered_map
// https://cplusplus.com/reference/algorithm/sort/

#include <iostream>
#include <array>
#include <unordered_map>
#include <string>
#include <algorithm>

bool descending_sort(int i, int j)
{
    return (i > j);
}

int main()
{
    std::array<int, 5> my_array = {1, 2, 3, 4, 5};

    for (int i = 0; i < my_array.size(); i++)
        std::cout << my_array[i] << ' ';

    std::cout << "\n------" << std::endl;

    // Range-based for loop using auto
    for (auto val : my_array)
        std::cout << val << ' ';

    std::cout << "\n--------------" << std::endl;

    // Basic for loop using iterators
    for (auto it = my_array.begin(); it < std::end(my_array); it++)
        // it is a pointer to the value
        std::cout << *it << ' ';
    // '*it' is the value of the iterator

    std::cout << "\n--------------" << std::endl;

    std::unordered_map<std::string, int> map;
    map["valorant"] = 2;
    map["csgo"] = 10;
    map["chess"] = 8;

    // using keyword can be used to define a type alias
    // iterator is a pointer to the value
    using MapType = std::unordered_map<std::string, int>::iterator;

    for (MapType it = map.begin(); it != map.end(); it++)
        std::cout << it->first << " " << it->second << '\n';

    std::cout << "\n--------------" << std::endl;

    // a range-based for loop with auto&
    for (auto &kv : map)
    {
        auto &key = kv.first;
        auto &val = kv.second;
        std::cout << key << " " << val << '\n';
    }
    // just using auto key and auto val will create a copy of the key and value
    // for large objects, this will potentially increase the time complexity
    
    std::cout << "\n--------------" << std::endl;
    

    // a range-based for loop with structured bindings
    for (const auto &[key, val] : map)
        std::cout << key << " " << val << '\n';

    std::cout << "\n--------------" << std::endl;

    // sort
    std::array<int, 5> my_array2 = {56, 98, 23, 54, 89};

    std::sort(my_array2.begin(), my_array2.end());
    for (auto val : my_array2)
        std::cout << val << ' ';

    std::cout << "\n--------------" << std::endl;

    int myints[] = {1, 2, 3, 4, 5, 4, 3, 2, 1};

    // custom sort function
    std::sort(myints, myints + 9, descending_sort); // 1 1 2 2 3 3 4 4 5

    for (int i = 0; i < 9; i++)
        std::cout << myints[i] << ' ';

    std::cout << "\n--------------" << std::endl;

    // Binary sort
    std::cout << "looking for 6... ";
    // it takes 4 arguments:
    // start of the array
    // end of the array
    // value to be searched
    // the sort function

    if (std::binary_search(myints, myints + 9, 6, descending_sort))
        std::cout << "found!\n";
    else
        std::cout << "not found.\n";

    return 0;
}