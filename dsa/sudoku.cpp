#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

bool isValid(vector<vector<string>> board,string c, int row, int col){
    for(int i=0;i<9;i++){
        if(board[i][col]==c||board[row][i]==c||board[3*(row/3)+i/3][3*(col/3)+i%3]==c) return false;
    }
    
    return true;
}
bool isValidSudoku(vector<vector<string>>& board) {
    for(int i=0;i<board.size();i++){
        for(int j=0;j<board[0].size();j++){
            if(board[i][j]!="."){
                string str = board[i][j];
                board[i][j]=".";
                if(!isValid(board,str,i,j)) {
                    board[i][j]=str;
                    return false;
                }
                board[i][j]=str;
            }
        }
    }
    return true;
}

int main(){
    vector<vector<string>> board = {{"5","3",".",".","7",".",".",".","."},{"6",".",".","1","9","5",".",".","."},{".","9","8",".",".",".",".","6","."},{"8",".",".",".","6",".",".",".","3"},{"4",".",".","8",".","3",".",".","1"},{"7",".",".",".","2",".",".",".","6"},{".","6",".",".",".",".","2","8","."},{".",".",".","4","1","9",".",".","5"},{".",".",".",".","8",".",".","7","9"}};
    if(isValidSudoku(board)) cout<<"yes";
    else cout<<"no";
    return 0;
}