#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    string s = "abcd";
    string rev = s;
    reverse(rev.begin(),rev.end());
    for(int i=0;i<rev.length();i++){
        if(s[i]!=rev[i]){
            s.insert(i,"");
        }
    }
    return 0;
}