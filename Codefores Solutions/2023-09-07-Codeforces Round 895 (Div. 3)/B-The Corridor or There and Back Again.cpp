// Link to Problem Statement
// https://codeforces.com/contest/1872/problem/B

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int test; cin >> test;
    while (test--)
    {
      int n; cin >> n;
      vector<int>  lst(202, -1);
      vector<bool> grid(500, true);
      for (int x = 0; x < n; x++)
      {
        int t, p; cin >> t >> p;
        grid[t + (p - 1) / 2] = false;
      }
      for (int x = 0; x < 500; x++)
      {
        if (grid[x] == false)
        {
          cout << x << "\n";
          break;
        }
      }
    }
    return 0;
}
