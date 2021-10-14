#include <bits/stdc++.h>
using namespace std;

int main(){
    int mx_area = 0;
    vector<int> heights = {1,8,6,2,5,4,8,3,7};
    for(int i = 0; i < heights.size(); ++i){
        for(int j = i + 1; j < heights.size(); ++j){
            int S = min(heights[i], heights[j]) * (j - i);
            if(S >= mx_area) mx_area = S;
        }
    }
    cout << mx_area;
}