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

bool isSafe(vector<string> &board, int row, int col,int n){
    int tempRow = row;
    int tempCol = col;
    while(tempRow>=0 && tempCol>=0){
        if(board[tempRow][tempCol]=='Q') return false;
        tempRow--;tempCol--;
    }
    tempCol=col;
    tempRow = row;
    while(tempCol>=0){
        if(board[tempRow][tempCol]=='Q') return false;
        tempCol--;
    }
    tempCol=col;
    tempRow = row;
    while(tempRow<n && tempCol>=0){
        if(board[tempRow][tempCol]=='Q') return false;
        tempRow++;tempCol--;
    }
    return true;
}

void placeQueen(int n, vector<string> &board, int col){
    if(col == n) return printArray(board);
    for(int row=0;row<n;row++){
        if(isSafe(board,row,col,n)){
            board[row][col] = 'Q';
            placeQueen(n,board,col+1);
            board[row][col] = '.';
        }
    }
}

int main(){
    int n = 4;
    string str(n,'.');
    vector<string> board(n,str);
    placeQueen(n,board,0);
    return 0;
}