// Priority Queue is part of STL, Import it with #include <queue>
// Generally used with heap data structure (heap is a complete binary tree)

// Applications:

// 1. Dijkstra's Algorithm
// 2. Prim's Algorithm
// 3. Huffman Coding
// 4. Heap Sort
// 5. Order Statistics
// 6. Priority Scheduling

// Priority Queue is a container adaptor that provides constant time O(1) lookup of the largest (by default) element, at the expense of logarithmic insertion and extraction.
// By default it is Max Priority Queue (Max Heap)

#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>

struct Comparison
{
    bool operator()(const int &lhs, const int &rhs) const
    {
        return lhs > rhs;
    }
};

int main()
{

    std::cout << "Max Priority Queue" << std::endl;

    std::priority_queue<int> pq;
    pq.push(10);
    pq.push(1);
    pq.push(100);
    pq.push(0);
    while (!pq.empty())
    {
        std::cout << pq.top() << " ";
        pq.pop();
    }

    std::cout << "\n-----------" << std::endl;

    // Priority Queue with Custom comparison function ==========
    std::cout << "Min Priority Queue" << std::endl;

    std::priority_queue<int, std::vector<int>, Comparison> pqCustom;

    pqCustom.push(10);
    pqCustom.push(1);
    pqCustom.push(100);
    pqCustom.push(0);
    while (!pqCustom.empty())
    {
        std::cout << pqCustom.top() << " ";
        pqCustom.pop();
    }

    std::cout << "\n-----------" << std::endl;

    // Min priority queue
    // std::greater<int> makes the max priority queue act as a min priority queue
    std::cout << "Min Priority Queue" << std::endl;
    const auto data = {1, 8, 5, 6, 3, 4, 0, 9, 7, 2};

    // directly initialize the priority queue with the data

    std::priority_queue<int, std::vector<int>, std::greater<int>> minq(data.begin(), data.end());

    while (!minq.empty())
    {
        std::cout << minq.top() << ' ';
        minq.pop();
    }

    std::cout << "\n-----------" << std::endl;
}