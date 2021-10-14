#include <bits/stdc++.h>
using namespace std;

bool Div_X(int i, int x)
{
    if(i % x == 0) return true;
    else return false;
}

bool Div_Y(int i, int y)
{
    if(i % y != 0) return true;
    else return false;
}

int main()
{
    int n; cin >> n;
    vector<int> v;
    while(n--)
    {
        int i; cin >> i;
        v.push_back(i);
    }
    int x, y; cin >> x >> y;

    vector<int> ans;

    for(auto i : v)
    {
        if(Div_X(i, x) && Div_Y(i, y))
        {
            ans.push_back(i);
        }
    }

    if(ans.size() == 0) cout << -1;
    else
    {
        for(auto i : ans) cout << i << " ";
    }
}