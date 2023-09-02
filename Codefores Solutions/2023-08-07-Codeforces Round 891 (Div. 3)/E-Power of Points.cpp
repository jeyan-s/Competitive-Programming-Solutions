# Link to Problem Statement
# https://codeforces.com/contest/1857/problem/E

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int t;
    cin >> t;
    
    while (t--)
    {
      
      int n; cin >> n;
      long long prefix = 0, suffix = 0, helper, t;
      vector<int> lst(n), tmp(n);
      map<int, long long> Hash;
      
      for (int x = 0; x < n; x++)
      {
        cin >> lst[x];
        tmp[x] = lst[x];
        suffix += lst[x];
      }
      
      sort(lst.begin(), lst.end(), [&](int x, int y){return x > y;});
      
      // for (int x: lst) cout << x << ' ';
      // cout << '\n';
      
      for (int x = 0; x < n; x++)
      {
        helper = lst[x];
        t = prefix - (x * helper);
        prefix += helper;
        t += (n - x) * helper - suffix;
        suffix -= helper;
        Hash[helper] = t + n;
      }
      
      for (int x: tmp) cout << Hash[x] << ' ';
      cout << '\n';
    }
    
    return 0;
}
