// Link to Problem Statement
// https://codeforces.com/contest/1867/problem/C

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int test_case; cin >> test_case;
    while (test_case--)
    {
      
      int n, k, a, b, rslt = 0; cin >> n;
      vector<int> lst(n);
      unordered_map<int, int> Hash;
      
      for (int x = 0; x < n; x++) 
      {
        cin >> lst[x];
        Hash[lst[x]] += 1;
      }
      
        int Mex = -1;
        for (int x = 0; x <= n; x++)
        {
          if (Hash[x] == 0) 
          {
            Mex = x;
            cout << x << "\n";
            break;
          }
        }
        
        int y; cin >> y;
        while (y != -1)
        {
          if (y == -1) 
          {
            cout.flush();
            continue;
          }
          cout << y << "\n";
          cin >> y;
        }
      
      cout.flush();
      
    }
    return 0;
}
