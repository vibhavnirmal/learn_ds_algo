// g++ -std=c++2a -fconcepts -o vec_mem 6_vector_memory.cpp && ./vec_mem


#include <iostream>
#include <vector>
#include <memory>

void print(std::vector<int> &vector) {
    for(auto value : vector) {
        std::cout << value << ' ';
    }
    std::cout << '\n';
}

int main() {
    /* ---------------------------------------------- */

    std::unique_ptr<int> ptr1(new int(5));
    std::cout << *ptr1 << '\n';

    ptr1.reset();
    std::cout << "----------------------------------------------" <<std::endl;

    std::shared_ptr<int> ptr2(new int(10));
    std::shared_ptr<int> ptr3(ptr2);

    std::cout << *ptr2 << ' ' << &ptr2 << std::endl;
    std::cout << *ptr3 << ' ' << &ptr3 << std::endl;

    ptr2.reset();
    ptr3.reset();

    std::cout << "----------------------------------------------" <<std::endl;

    // make_shared() is a factory function that creates a shared_ptr
    auto ptr_1 = std::make_shared<int[]>(10);
    auto ptr_2 = ptr_1;

    // use_count() returns the number of shared_ptr objects
    // shared pointer means that the object is shared between multiple pointers

    std::cout << "Reference count: " << ptr_1.use_count() << '\n';

    ptr_1.reset();
    ptr_2.reset();

    std::cout << "----------------------------------------------" <<std::endl;

    auto ptr = std::make_unique<int[]>(10);
    for(int i = 0; i < 10; i += 1) {
        ptr[i] = i * i;
    }
    std::cout << ptr[5] << '\n';
    std::cout << ptr[9] << '\n';

    ptr.reset();

    std::cout << "----------------------------------------------" <<std::endl;

    std::vector<int> my_vector;
    my_vector.reserve(5);

    for(int i = 1; i <= 10; ++i) {
        std::cout << "Size: " << my_vector.size() << '\n';
        std::cout << "Capacity: " << my_vector.capacity() << '\n';
        my_vector.push_back(i);
    }
}
