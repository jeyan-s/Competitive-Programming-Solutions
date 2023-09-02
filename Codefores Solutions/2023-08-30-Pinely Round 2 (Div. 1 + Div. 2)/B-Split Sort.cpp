// Link to problem Statement
// https://codeforces.com/contest/1863/problem/B

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int test_case; cin >> test_case;
    while (test_case--)
    {
      int n, rslt = 0; cin >> n;
      vector<int> lst(n);
      unordered_map<int, int> Hash;
      for (int x = 0; x < n; x++) 
      {
        cin >> lst[x];
        Hash[lst[x]] = x;
      }
      while (n > 1)
      {
        if (Hash[n - 1] > Hash[n]) rslt++;
        n--;
      }
      cout << rslt << '\n';
    }
    return 0;
}
