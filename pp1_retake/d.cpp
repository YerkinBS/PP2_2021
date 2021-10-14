#include <bits/stdc++.h>
using namespace std;

int main()
{
    string a, b, c;
    cin >> a; cin >> b; cin >> c;
    string all = a + b + c;
    string alphabet = "abcdefghijklmnopqrstuvwxyz";

    for(int i = 0; i < alphabet.size(); i++)
    {
        if(all.find(alphabet[i]) == -1) cout << alphabet[i];
    }
}