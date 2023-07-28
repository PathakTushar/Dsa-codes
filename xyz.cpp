// C++ implementation to find nCr
#include <bits/stdc++.h>
using namespace std;

// Driver code
int main()
{
    int t, n, q;
    cin >> t;
    while (t--)
    {
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
        // int ncr=printNcR(n,2);
        int res = (10 - n) * (9 - n) * 3;
        cout << res << endl;
    }

    return 0;
}
