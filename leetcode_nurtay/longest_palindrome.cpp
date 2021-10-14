#include <bits/stdc++.h>
using namespace std;

bool Palindrome_Check(string s){
    for(int i = 0; i < s.size(); i++){
            if(s[i] != s[s.size()-i-1]) return false;
    }
    return true;
}

void solve(){
    string s; cin >> s;
    vector<string> palindromes;
    for(int i = 0; i < s.size(); i++){
        for(int j = 1; j <= s.size() - i; j++){
            string t = s.substr(i, j);
            if(Palindrome_Check(t)) palindromes.push_back(t);
        }
    }

    sort(palindromes.begin(), palindromes.end(), []
    (const std::string& first, const std::string& second){
        return first.size() < second.size();
    });

    cout << s.size();

    cout << palindromes[palindromes.size()-1];
}


int main(){
    solve();
}