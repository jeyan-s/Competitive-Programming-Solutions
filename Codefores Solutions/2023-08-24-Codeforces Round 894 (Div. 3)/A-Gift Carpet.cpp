// Link to Problem Statement
// https://codeforces.com/contest/1862/problem/A

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int test_cases; cin >> test_cases;
    
    while (test_cases--)
    {
      int n, m; cin >> n >> m;
      bool v, i, k, a, c;
      v = i = k = a = c = false;
      vector<string> lst(n);
      for (int x = 0; x < n; x++) cin >> lst[x];
      for (int y = 0; y < m; y++)
      {
        for (int x = 0; x < n; x++)
        {
          if (!v && lst[x][y] == 'v') 
          {
            v = true;
            break;
          }
          else if (v && !i && lst[x][y] == 'i') 
          {
            i = true;
            break;
          }
          else if (v && i && !k && lst[x][y] == 'k') 
          {
            k = true;
            break;
          }
          else if (v && i && k && !a && lst[x][y] == 'a') 
          {
            a = true;
            break;
          }
        }
      }
      bool rslt = v && i && k && a;
      if (rslt) cout << "YES" << '\n';
      else cout << "NO" << '\n';
      // cout << c;
    }
    
    return 0;
}
