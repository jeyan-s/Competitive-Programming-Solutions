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
      int n, k; cin >> n;
      vector<int> lst(n);
      
      for (int x = 0; x < n; x++) cin >> lst[x];
      int prev = lst[0], Found = false;
      sort(lst.begin(), lst.end());
      
      for (int x = 0; x < n; x++)
      {
        if (prev != lst[x]) Found = true;
      }
      
      if (!Found) 
      {
        cout << -1 << '\n';
        continue;
      }
      
      int t = count(lst.begin(), lst.end(), lst[0]);
      cout << t << ' ' << n - t << '\n';
      for (int x = 0; x < t; x++)
      {
        cout << lst[x] << ' ';
      }
      
      cout << '\n';
      
      for (int x = t; x < n; x++)
      {
        cout << lst[x] << ' ';
      }
      
      cout << '\n';
      
    }
    
    return 0;
}
