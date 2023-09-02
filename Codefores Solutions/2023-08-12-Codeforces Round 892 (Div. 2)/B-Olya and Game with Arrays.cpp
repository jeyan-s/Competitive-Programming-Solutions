// Link to Problem Statement
// https://codeforces.com/contest/1859/problem/A

#include <bits/stdc++.h>
using namespace std;

int solve()
{
  return 9;
}

int main() 
{
    int t; cin >> t;
    
    while (t--)
    {
      int n, first_min = INT_MAX, second_min = INT_MAX;
      cin >> n;
      long long Sum = 0;
      for (int x = 0; x < n; x++)
      {
        int m; cin >> m;
        vector<int> lst(m);
        
        for (int y = 0; y < m; y++)
        {
          cin >> lst[y];
        }
        
        sort(lst.begin(), lst.end());
        
        first_min = min(first_min, lst[0]);
        second_min = min(second_min, lst[1]);
        Sum += (long long) lst[1];
        // for (int y = 0; y < m; y++) cout << lst[y] << '\n';
      }
      // cout << Sum << ' ' << first_min << ' ' << second_min << '\n';
      cout << Sum + (long long) first_min - (long long) second_min << '\n';
    }
    
    return 0;
}
