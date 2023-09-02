// Link to Problem Statement
// https://codeforces.com/contest/1862/problem/C

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int test_Cases; cin >> test_Cases;
    while (test_Cases--)
    {
      int n; cin >> n;
      vector<int> lst(n), prefix(n, 0);
      bool Error = false;
      for (int x = 0; x < n; x++) cin >> lst[x];
      for (int x = 0; x < n; x++)
      {
        prefix[0] -= 1;
        if (lst[x] < n) prefix[lst[x]] += 1;
      }
      for (int x = 1; x < n; x++) 
      {
        prefix[x] = prefix[x] + prefix[x - 1];
      }
      for (int x = 0; x < n; x++) 
      {
        prefix[x] += lst[x];
        if (prefix[x] != 0) 
        {
          Error = true;
          break;
        }
      }
      // for (int x: prefix) cout << x << ' ';
      if (Error) cout << "NO\n";
      else cout << "YES\n";
    }
    return 0;
}
