#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

long long totalCost(vector<int>& costs, int k, int candidates) {
    long long res = 0;
    for(int i=0;i<k;i++){
        int min1,min2,temp;
        if(candidates<costs.size()){
            min1 = *min_element(costs.begin(),costs.begin()+candidates);
            min2 = *min_element(costs.end()-candidates,costs.end());
            temp = min(min1,min2);  
        }
        else{
            temp = *min_element(costs.begin(),costs.end());
        }
        res+=temp;
        auto it = find(costs.begin(),costs.end(),temp);
        int ind = it - costs.begin();
        costs.erase(costs.begin()+ind);
    }
    return res;
}
int main(){
    vector<int> costs = {50,80,34,9,86,20,67,94,65,82,40,79,74,92,84,37,19,16,85,20,79,25,89,55,67,84,3,79,38,16,44,2,54,58};
    long long val = totalCost(costs,7,12);
    cout<<val<<endl;
    return 0;
}