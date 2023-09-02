// Link to problem Statement
// https://codeforces.com/contest/1863/problem/C

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int test_case; cin >> test_case;
    while (test_case--)
    {
      
      int n, k, Mex = -1, left = 0; cin >> n >> k;
      vector<int> lst(n), new_lst(n + 1), mex_lst(n, -1);
      unordered_map<int, int> Hash;
      
      for (int x = 0; x < n; x++) 
      {
        cin >> lst[x];
        Hash[lst[x]]++;
      }
      
      for (int x = 0; x <= n; x++)
      {
        if (Hash[x] == 0)
        {
          Mex = x;
          break;
        }
      }
      
      // cout << Mex << '\n';
      // new_lst[0] = Mex;
      
      for (int x = 0; x < n - 1; x++) 
      {
        new_lst[x] = lst[x + 1];
      }
      
      
      new_lst[n - 1] = Mex;
      new_lst[n] = lst[0];
      
      // for (int x: new_lst) cout << x << ' ';
      // cout << "\n";
      
      
      int K = n, x = k % (n + 1);
      x = n - x;
      // cout << x << 'a' <<'\n';
      
      while (K--)
      {
        cout << new_lst[x++] << ' ';
        x %= (n + 1);
      }
      
      cout << "\n";
      
    }
    return 0;
}
