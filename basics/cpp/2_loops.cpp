// g++ -std=c++2a -o loops 2_loops.cpp && ./loops

#include <iostream>
#include <array>

using namespace std;

int main(){
    /* --------------------------------------------------   */
    
    cout << "using array :->" << endl;

    // array is a container that encapsulates fixed size arrays

    // array is a template class that takes two parameters: the type of the elements and the size of the array
    // arrays size is fixed and cannot be changed (unlike vectors)
    // arrays are like tuples in python with fixed size
    // vectors are like lists in python with dynamic size

    array<int, 5> my_array = {45, 23, 3, 10, 40};
    cout << "my_array is [45, 23, 3, 10, 40]" << endl;

    cout << "Size of array = " << my_array.size() << '\n';
    cout << "First element of the array is " << my_array[0] << '\n'; // first element

    int array_size = my_array.size();
    // Declaring array_size variable and assigning it to my_array.size()

    cout << "--------------" << endl;
    /* --------------------------------------------------   */

    cout << "Array iteration with for loop :->" << endl;

    // for loop is used to execute a block of code a number of times
    for (int i = 0; i < array_size; i += 1)
        cout << "i:" << i << " > element:" << my_array[i] << '\n';

    // ranged for loop is used to iterate over a range of elements
    cout << "Iterating elements using the ranged for loop" << endl;
    for (int value : my_array)
        cout << value << ' ';

    cout << "\n--------------" << endl;
    cout << "Array iteration with while loop :->" << endl;

    while (array_size > 0)
    {
        array_size -= 1;
        cout << "i:" << array_size << " > element:" << my_array[array_size] << '\n';
    }

    // array_size variable has been changed in the while loop and now it is 0
    cout << "array_size is " << array_size << endl;

    cout << "--------------" << endl;

    // do while loop is used to execute a block of code at least once
    cout << "Array iteration with do while loop :->" << endl;
    // reassigning array_size to my_array.size()
    array_size = my_array.size();
    // define a temp variable and assign it to 0
    int temp = 0;
    do
    {
        cout << "i:" << temp << " > element:" << my_array[temp] << '\n';
        temp += 1;
    } while (temp < array_size);

    cout << "--------------" << endl;

    // switch statement is used to execute a block of code depending on the value of a variable
    cout << "switch statement :->" << endl;
    int switch_var = 4;
    switch (switch_var)
    {
    case 1:
        cout << "switch_var is 1" << endl;
        break;
    case 2:
        cout << "switch_var is 2" << endl;
        break;
    case 3:
    case 4:
        cout << "switch_var is 4 without break" << endl;
    default:
        cout << "switch_var is not 1 or 2" << endl;
        break;
    }

    cout << "--------------" << endl;
    /* --------------------------------------------------   */

    // goto statement is used to jump to a label
    cout << "goto statement :->" << endl;
    int n = 10;
mylabel:
    cout << n << ", ";
    n--;
    if (n > 0)
        goto mylabel;
    cout << "liftoff!\n";

    cout << "--------------" << endl;

    return 0;
}