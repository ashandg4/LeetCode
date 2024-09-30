// Subtract the Product and Sum of Digits of an Integer

#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "Enter the number: ";
    cin >> n;

    int prod = 1;
    int sum = 0;

    while (n != 0)
    {
        int digit = n % 10;
        sum += digit;
        prod *= digit;

        n /= 10;
    }
    int answer = prod - sum;
    cout << "Output: " << answer << endl;
}