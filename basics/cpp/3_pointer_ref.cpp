// g++ -std=c++2a -o pointer_ref 3_pointer_ref.cpp && ./pointer_ref

// pointers and references are used to access the memory address of a variable
// dynamic memory allocation is used to allocate memory at run time
// new and delete are used to allocate and deallocate memory

#include <iostream>
#include <string>

using namespace std;

int main()
{
    /* --------------------------------------------------   */
    // reference is an alias for another variable
    int p = 5; // p = 5
    int q = p; // q = 5
    q += 1;    // q = 6

    // p and q are two different variables with two different memory addresses
    cout << "&p = " << &p << '\n';
    cout << "&q = " << &q << '\n';
    // & symbol is used to get the memory address of a variable

    // r is a reference to p which means that r is an alias for p
    // it does not have its own memory address
    // it does not create a new variable / memory location
    cout << "--------------" << endl;

    int &r = p; // r = p = 5
    p += 2;     // p = 7 and therefore r = 7
    cout << "&r = " << &r << '\n';
    cout << "r = " << r << '\n';

    // s is a copy of r which makes s a copy of p and creates a new memory location
    int s = *(&r); // s = 7

    // pointer is a variable that stores the memory address of another variable
    // it is declared with the * symbol
    cout << "&s = " << &s << '\n';

    int *ps = &s; // ps = memory address of s (pointer to s)
    *ps += 1;     // s = 8

    cout << "--------------" << endl;
    /* --------------------------------------------------   */

    // dynamic memory allocation is the process of allocating memory at run time
    // it is used to allocate memory for objects whose size is not known at compile time
    // int_ptr is a pointer to an integer
    // new int[10] allocates memory for an array of 10 integers
    // the memory address of the first element of the array is stored in int_ptr
    int *int_ptr = new int[10];
    int_ptr[5] = 241;
    cout << "Value " << int_ptr[5] << '\n';
    cout << "Address " << &int_ptr[5] << '\n';

    // int_ptr[4] is the same as *(int_ptr + 4)
    // the value of the 5th element will be 0 because it has not been initialized
    cout << "Value " << int_ptr[4] << '\n';
    cout << "Address " << &int_ptr[4] << '\n';

    // delete[] is used to deallocate the memory
    // it also calls the destructor of the objects and frees the memory
    delete[] int_ptr;

    // delete int_ptr; // this will cause an error because int_ptr is a pointer to an array of integers

    // string *str_ptr = new string[10];
    // str_ptr[5] = "Hello";
    // cout << "Value " << str_ptr[5] << '\n';
    // cout << "Address " << &str_ptr[5] << '\n';
    // delete[] str_ptr;
    cout << "--------------" << endl;

    int *pp = new int;
    // pp is a pointer to an integer
    *pp = 5; // the value of that integer is 5
    cout << "Value " << *pp << '\n';
    cout << "Address " << pp << '\n';

    // return is not required in main function
}