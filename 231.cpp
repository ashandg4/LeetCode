// Power of Two

#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int n;
    cout << "Enter the number: ";
    cin >> n;

    for (int i = 0; i <= 30; i++)
    {
        int ans = pow(2, i);
        if (ans == n)
        {
            cout << true;
            break;
        }
        else
        {
            cout << false;
        }
    }

    // int i = 0;
    // while (i <= 30)
    // {
    //     int ans = pow(2, i);
    //     if (ans == n)
    //     {
    //         cout << true;
    //         break;
    //     }
    //     else
    //     {
    //         cout << false;
    //     }
    //     i++;
    // }
}