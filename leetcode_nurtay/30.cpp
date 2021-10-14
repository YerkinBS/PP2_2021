#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

int main()
{ 
    // string s = "barfoothefoobarman";
    // vector<string> v = {"foo","bar"};

    string s = "aaaaaaaaaaaaaa";
    vector<string> v = {"aa","aa"};


    // string s = "foobarfoobar";
    // vector<string> v = {"foo","bar"};

    // string s = "lingmindraboofooowingdingbarrwingmonkeypoundcake";
    // vector<string> v = {"fooo","barr","wing","ding","wing"};

    vector<int> ans;
    string x = "";
    sort(v.begin(), v.end());
    do
    {
        for(auto i : v) x += i;
        int j = 0;
        while(j < s.size())
        {
            string t = s.substr(j, x.size());
            if(x == t) ans.push_back(j);
            j++;
        }
        x = "";
    }
    while(next_permutation(v.begin(), v.end()));


    for(auto i : ans) cout << i << " ";
}