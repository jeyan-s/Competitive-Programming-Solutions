// Link to Problem Statement
// https://codeforces.com/contest/1879/problem/A

#include <bits/stdc++.h>
 
using namespace std;
 
int main() 
{
    int test_case; cin >> test_case;
    while (test_case--)
    {
      // int n, k, a, b, rslt = 0; cin >> n;
      // vector<int> lst(n);
      // for (int x = 0; x < n; x++) cin >> lst[x];
      int n, a, b, op = 0; cin >> n;
      cin >> a >> b;
      
      for (int x = 1; x < n; x++)
      {
        int t, p;
        cin >> t >> p;
        if (t >= a) op = max(p, op);
      }
      if (b > op) cout << a << "\n";
      else cout << -1 << "\n";
      
    }
    return 0;
}
