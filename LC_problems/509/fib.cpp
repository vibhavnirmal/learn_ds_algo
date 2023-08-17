// https://leetcode.com/problems/fibonacci-number/

// Write a program in C++ that takes a positive integer n as input from the user and prints the first n Fibonacci numbers using a vector.
// A Fibonacci number is the sum of the previous two Fibonacci numbers, starting from 0 and 1.
// For example, the first 10 Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

// https://leetcode.com/problems/fibonacci-number/
// 509. Fibonacci Number

// Used vectors (lists of python), do while loop, memoization

// g++ -o fibonacci fib.cpp

#include <iostream>
#include <vector>

std::vector<int> fibonacci(int total)
{
    int first = 0;
    int second = 1;
    std::vector<int> fib;
    if (total >= 1)
        fib.push_back(first);
    if (total >= 2)
        fib.push_back(second);

    for (int i = 2; i <= total; i++)
    {
        int next = fib[i - 1] + fib[i - 2];
        fib.push_back(next);
    }

    return fib;
}

int fib_mem(int total, std::vector<int> &dp)
{
    if (total == 0)
        dp[total] = 0;
    if (total == 1)
        dp[total] = 1;

    if (dp[total] != -1)
        return dp[total];

    return dp[total] = fib_mem(total - 1, dp) + fib_mem(total - 2, dp);
}

int main()
{
    int total;
    do
    {
        std::cout << "How many Fibonacci numbers would you like? (has to be > 0)" << std::endl;
        std::cin >> total;
    } while (total <= 0);

    std::cout << "Method 1: For loop" << std::endl;
    std::cout << "Method 2: Recurrence Function" << std::endl;
    std::cout << "Method 3: Memoization" << std::endl;

    std::cout << "-----------------" << std::endl;

    int method;
    std::cout << "Which method would you like? (choose Number)" << std::endl;
    std::cin >> method;

    int first = 0, second = 1, next;

    if (method == 1)
    {
        if (total == 1)
        {
            std::cout << first;
            return 0;
        }
        else if (total == 2)
        {
            std::cout << first << "," << second;
            return 0;
        }
        else
        {
            std::cout << first;
            for (int i = 0; i < total - 1; i++)
            {
                std::cout << "," << second;
                next = first + second;
                first = second;
                second = next;
            }
        }
    }
    else if (method == 2)
    {
        total = total - 1;
        std::vector<int> myFib = fibonacci(total);
        std::cout << myFib[0];
        for (int i = 1; i < myFib.size(); i++)
        {
            std::cout << "," << myFib[i];
        }
    }
    else if (method == 3)
    {
        // memoization
        std::vector<int> storage(total + 1, -1);

        for (int i = 0; i < total; i++)
        {
            std::cout << fib_mem(i, storage) << ",";
        }
    }
    else
    {
        std::cout << "Choose from 1,2 or 3" << std::endl;
    }
}