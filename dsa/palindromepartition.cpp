#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

void printArray(vector<string> &arr){
    for(auto it : arr){
        cout<<it<<" ";
    }
    cout<<endl;
}

bool isValid(string s){
    string rev = s;

    reverse(rev.begin(), rev.end());
 
    if (s == rev) return true;
    else return false;
 
}

void partition(vector<string> &temp, string s, int len, int pin){
    if(pin==len){
        return printArray(temp);
    }
    for(int i = pin;i<len;i++){
        string str = s.substr(pin,i+1-pin);
        if(isValid(str)){
            temp.push_back(str);
            partition(temp,s,len,i+1);
            temp.pop_back();
        }
    }

}

int main(){
    vector<string> temp;
    string s = "aabb";
    int len = s.length();
    partition(temp,s,len,0);
    return 0;
}