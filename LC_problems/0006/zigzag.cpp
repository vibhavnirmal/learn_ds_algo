#include <iostream>
#include <vector>
#include <string>

using namespace std;

string convert(string s, int numRows){
    if (numRows <= 1)
        return s;

    // Create a vector of strings to store all the rows
    vector<string> v(numRows, "");

    // j is the row index we are currently on
    // dir is the direction we are travelling in
    int j = 0, dir = -1;

    // Loop through the string
    for (int i = 0; i < s.length(); i++){
        // If we are at the top or bottom row, we change direction
        if (j == numRows - 1 || j == 0)
            dir *= (-1);

        // Add the current character to the current row
        v[j] += s[i];

        // Update our row index
        if (dir == 1)
            j++;
        else
            j--;
    }

    // Concatenate all the rows together
    string res;

    for (auto &it : v)
        res += it;

    // Return the result
    return res;
}

int main()
{
    cout<<convert("A", 1)<<endl;
    cout<<convert("PAYPALISHIRING", 3)<<endl;
    cout<<convert("PAYPALISHIRING", 4)<<endl;


    return 0;
}