#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n; cin >> n;
    int ans = 0;
    for(int i = 1; i <= n; i++)
    {   
        int cnt = 0;
        string s = to_string(i);
        for(int j = 0; j < s.size(); j++)
        {
            cnt += int(s[j]);
        }
        if(cnt % 4 == 0) ans++;
    }
    cout << ans;
}