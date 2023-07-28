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

void findUniqueSubset(vector<int> arr, vector<int> temp, int curIn, int n){
    if(curIn == n) return;
    for(int i = curIn; i<n; i++){
        if(arr[i] == arr[i-1] && i>curIn) continue;
        temp.push_back(arr[i]);
        findUniqueSubset(arr,temp,i+1,n);
        printArray(temp);
        temp.pop_back();
    }
}

void findPermutation(vector<int> arr, vector<int> temp,vector<int> &visited, int n){
    if(temp.size() == n) return printArray(temp);
    for(int i=0;i<n;i++){
        if(visited[i]==0){
            temp.push_back(arr[i]);
            visited[i] = 1;
            findPermutation(arr,temp,visited,n);
            visited[i]=0;
            temp.pop_back();
        }
    }
}

void findPermutationBySwap(vector<int> &arr,int curIn, int n){
    if(curIn == n){
        return printArray(arr);
    }
    for(int i=curIn;i<n;i++){
        swap(arr[curIn],arr[i]);
        findPermutationBySwap(arr,curIn+1,n);
        swap(arr[curIn],arr[i]);
    }
}

int main(){
    vector<int> arr = {1,2,3};
    int n = arr.size();
    vector<int> temp;
    vector<int> visited(n,0);
    // findPermutation(arr,temp,visited,n);
    // findUniqueSubset(arr,temp,0,n);
    findPermutationBySwap(arr,0,n);
    return 0;
}