#include <bits/stdc++.h>
using namespace std;

bool Repeating_Check(string s){
    set<char> characters;
    for(int i = 0; i < s.size(); i++) characters.insert(s[i]);
    if(characters.size() == s.size()) return true;
    else return false;
}

int main(){
    string s; cin >> s;
    int mx_len = 0;

    for(int i = 0; i < s.size(); i++){
        for(int j = 1; j <= s.size() - i; j++){
            string t = s.substr(i, j);
            if(Repeating_Check(t) and t.size() > mx_len) mx_len = t.size(); 
        }
    }
    cout << mx_len;
}