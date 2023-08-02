// for g++ 9 and earlier:
// g++ -std=c++2a -fconcepts -o functions 4_functions.cpp && ./functions

// reference: https://en.cppreference.com/w/

#include <array>
#include <iostream>

using namespace std;

// --------------------------------------------------------------------------------
// void means that the function does not return a value
// array<int, 3> means that the function takes an array of integers as a parameter which has a size of 3
void print_array(array<int, 3> array) {
    for(int value : array) {
        cout << value << ' ';
    }
    cout << '\n';
}

// function overloading is when you have multiple functions with the same name but different parameters
void print_array(std::array<float, 3> array) {
    for (auto value : array) {
        cout << value << ' ';
    }
    cout << '\n';
}
// --------------------------------------------------------------------------------
// new c++ feature
// auto means that the type of the variable is automatically deduced from its initializer
// this is called type inference
// function templates are a way to write generic functions
void print_array_without_type(auto array) {
    for (auto value : array) {
        cout << value << ' ';
    }
    cout << '\n';
}
// --------------------------------------------------------------------------------
// int means that the function returns an integer
int sum(array<int, 3> array) {
    int sum = 0;
    
    for(int value : array) {
        sum += value;
    }

    return sum;
}
// --------------------------------------------------------------------------------
// generic function

// if we don't use '&' then the array will be passed by value (a copy of the array)
// the function will be creating a copy of the array and it will take more memory

// in auto& array the & means that array is passed by reference (the original array)
// this means that function is not creating a new copy of array

// we can use const auto& array to make sure that the function does not modify the array
// auto& array and auto &array are the same and space around & is doesn't matter
float mul(const auto &array) {
    // auto mul = 1;
    // value 1 will be treated as an integer and the result will be 26

    // to get the correct result we need to use a floating point number
    auto mul = 1.0f;

    for(auto value : array) {
        mul *= value;
    }
    return mul;
}

// template specialization
template<>
float mul(const array<int, 3> &array) {
    cout << "\nFrom the specialization!" << endl;
    int mul = 1;
    for(int value : array) {
        mul *= value;
    }
    return mul;
}
// --------------------------------------------------------------------------------


// main function is the entry point of the program
// it is where the program starts executing
int main() {
    cout << "--------------" << endl;

    cout << "Function overloading :->" << endl;
    array<int, 3> my_array_1 = {1, 2, 3};
    print_array(my_array_1);
    array<float, 3> my_array_2 = {4.4f, 5.5f, 6.6f};
    print_array(my_array_2);

    cout << "--------------" << endl;

    cout << "Using auto keyword for function parameters:->" << endl;
    print_array_without_type(my_array_1);
    print_array_without_type(my_array_2);
    
    cout << "--------------" << endl;

    array<int, 3> my_array_3 = {7, 8, 9};
    cout << "The sum of our array [7, 8, 9] is: " << sum(my_array_3) << '\n';

    cout << "--------------" << endl;

    array<int, 3> my_array_4 = {1, 2, 3};
    cout << "The product of our array [1, 2, 3] is: " << mul(my_array_4) << '\n';
    array<float, 4> my_array_5 = {1.1f, 2.2f, 3.3f, 4.4f};
    cout << "The product of our array [1.1, 2.2, 3.3, 4.4] is: " << mul(my_array_5) << '\n';

    cout << "--------------" << endl;



    return 0;
}
