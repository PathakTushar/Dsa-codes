#include <iostream>
#include <vector>
using namespace std;

// int partition(vector<int> &arr, int low, int high){
//     int pivot = arr[high];
//     int i = low-1;
//     for(int j=low;j<high;j++){
//         if(arr[j]<=pivot){
//             i++;
//             swap(arr[i],arr[j]);
//         }
//     }
//     swap(arr[i+1],arr[high]);
//     return i+1;
// }

// void quickSort(vector<int> &arr, int low, int high){
//     if(low<high){
//         int pi = partition(arr,low,high);
//         quickSort(arr,low,pi-1);
//         quickSort(arr,pi+1,high);
//     }
// }

void merge(vector<int> &arr, int low, int mid, int high){
    vector<int> temp;
    int left = low;
    int right = mid+1;

    while(left <= mid && right <= high){
        if(arr[left] <= arr [right]){
            temp.push_back(arr[left]);
            left++;
        }
        else{
            temp.push_back(arr[right]);
            right++;
        }
    }
    while(left<=mid){
        temp.push_back(arr[left]);
        left++;
    }
    while(right<=high){
        temp.push_back(arr[right]);
        right++;
    }
    for(int i=low; i<=high;i++){
        arr[i]=temp[i-low];
    }
}

void mergeSort(vector<int> &arr, int low, int high){
    if(low == high) return;
    int mid = (low + high) / 2;
    mergeSort(arr,low,mid);
    mergeSort(arr,mid+1,high);
    merge(arr,low,mid,high);
}

int main()
{
    vector<int> arr = {7,6,4,4,2,3,5};
    int n = arr.size();
    // quickSort(arr,0,n-1);
    mergeSort(arr,0,n-1);
    for(auto it : arr){
        cout<<it<<" ";
    }
    cout<<endl;
    return 0;
}