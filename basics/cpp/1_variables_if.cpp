// g++ -o basicFunctionalities 1_variables_if.cpp && ./basicFunctionalities

// C++ is a statically typed language, which means that all variables have a type that must be known at compile time.
// References: https://cplusplus.com/doc/tutorial/

// iostream is a header that defines the standard input/output stream objects
#include <iostream>
#include <string>

// #define is a preprocessor directive that tells the compiler to replace the text PI with the value 3.14159
#define PI 3.14159

// namespace is a way to organize code into logical groups and to prevent name collisions that can occur especially when your code base includes multiple libraries
using namespace std;

int main()
{

    // all variables must be declared before they are used

    int foo = 0;       // variable declaration with initialization
    decltype(foo) bar; // decltype returns the type of its operand

    int x = 5;      // initial value: 5 assignment initialization
    int y(3);       // initial value: 3 constructor initialization
    float z{2.02f}; // initial value: 2 uniform initialization
    int result;     // initial value undetermined (garbage value)

    string my_str = "Hello World!";

    // All of the following are equivalent ways of initializing a string
    // string mystring = "This is a string";
    // string mystring ("This is a string");
    // string mystring {"This is a string"};

    cout << "x is " << x << ", y is " << y << " and z is " << z << endl;
    cout << "Type of x can be determined by typeid keyword" << endl;
    cout << "typeid(x).name() :  " << typeid(x).name() << endl;
    cout << "typeid(z).name() :  " << typeid(z).name() << endl;
    cout << "typeid(s).name() :  " << typeid(my_str).name() << endl;

    cout << "result is " << result << endl;

    cout << "--------------" << endl;
    /* --------------------------------------------------   */

    cout << "Using auto keyword for sum :->" << endl;
    // variables are declared with the type and name
    // auto type means that the compiler will deduce the type of the variable
    auto var1 = 23;
    auto var2 = 32;
    auto var3 = var1 + var2;

    // cout is an object of the class ostream (output stream)
    // << is the insertion operator
    // endl is the end of line operator
    // '/n' is the new line operator
    cout << "var1 is " << var1 << endl;
    cout << "var2 is " << var2 << endl;
    cout << "var3 is var1 + var2 = " << var3 << endl;
    cout << "Here var1 var2 and var3 has auto datatype" << endl;

    cout << "--------------" << endl;
    /* --------------------------------------------------   */

    cout << "Using auto keyword for string :->" << endl;
    // new c++ feature
    // auto g;
    // above line will give error: declaration of ‘auto var’ has no initializer with old c++ compilers

    auto g = "Hello World!";
    cout << "g is " << g << endl;

    // if statement is used to execute a block of code if a condition is true
    int a = 15;
    int b = 10;

    cout << "--------------" << endl;
    /* --------------------------------------------------   */

    cout << "if statement :->" << endl;

    cout << "a is " << a << endl;
    cout << "b is " << b << endl;

    if (a < b)
    {
        cout << "a is less than b!\n";
    }
    else if (a == b)
    {
        cout << "a is equal to b!\n";
    }
    else
    {
        cout << "a is greater than b!\n";
        if (a == 15)
        {
            std::cout << "a is equal to 15!\n";
        }
    }

    cout << "--------------" << endl;

    /* --------------------------------------------------   */
    return 0;
}
