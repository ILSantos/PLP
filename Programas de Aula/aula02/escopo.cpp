#include <iostream>
using std::cout;
int main()
{
    int x = 0;
    {
        int x = 10;
        cout << x << "\n";
    }
    cout << x << "\n";   
}
