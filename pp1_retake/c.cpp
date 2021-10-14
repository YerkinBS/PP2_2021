#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n; cin >> n;
    int sum = 0;
    vector<char> v;
    while(n--)
    {
        char x; cin >> x;
        v.push_back(x);
    }

    for(auto i : v)
    {
        sum += int(i);
    }
    cout << sum;
}