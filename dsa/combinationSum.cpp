#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void printArray(vector<int> &arr){
    for(auto it : arr){
        cout<<it<<" ";
    }
    cout<<endl;
}

void findCombination(vector<int> &arr, vector<int> &temp, int curIn, int n, int sum){
    if(curIn == n) return;
    if(sum == 0){
        return printArray(temp);
    }
    if(arr[curIn]<=sum){
        temp.push_back(arr[curIn]);
        findCombination(arr,temp,curIn,n,sum-arr[curIn]);
        temp.pop_back();
    }
    findCombination(arr,temp,curIn+1,n,sum);
}
void findSecondCombination(vector<int> &arr, vector<int> &temp, int curIn, int n, int sum){
    // if(curIn == n) return;
    if(sum==0){
        return printArray(temp);
    }
    for(int i=curIn;i<n;i++){
        if(i>curIn && arr[i]==arr[i-1]){
            continue;
        }
        if(arr[i]>sum) break;
        temp.push_back(arr[i]);
        findSecondCombination(arr,temp,i+1,n,sum-arr[i]);
        temp.pop_back();
    }
}
void findThirdCombination(vector<int> &arr, vector<int> &temp, int curIn, int n, int sum){
    if(curIn == n){
        temp.push_back(sum);
        return;
    }
    findThirdCombination(arr,temp,curIn+1,n,sum+arr[curIn]);
    findThirdCombination(arr,temp,curIn+1,n,sum);
}
int main(){
    cout<<"Combination Sum one\n";
    vector<int> arr = {2,3,4,7};
    vector<int> temp;
    int n = arr.size();
    findCombination(arr,temp,0,n,7);
    cout<<"Combination Sum Two\n";
    vector<int> arr2 = {1,2,1,2,1};
    sort(arr2.begin(), arr2.end());
    vector<int> temp2;
    int n2 = arr2.size();
    findSecondCombination(arr2,temp2,0,n2,4);
    cout<<"Combination Sum Three\n";
    vector<int> arr3 = {2,3,1};
    vector<int> temp3;
    int n3 = arr3.size();
    findThirdCombination(arr3,temp3,0,n3,0);
    printArray(temp3);
}