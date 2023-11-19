// Link to Problem Statement
// https://codeforces.com/contest/1879/problem/B

#include <bits/stdc++.h>

using namespace std;

int main() 
{
    int test_case; cin >> test_case;
    while (test_case--)
    {
      long long n, s1 = 0, s2 = 0, m1 = int(1e10), m2 = int(1e10), rslt = 0; cin >> n;
      vector<long long> lst(n), lst1(n);
      for (int x = 0; x < n; x++) 
      {
        cin >> lst[x];
        s1 += lst[x];
        m1 = min(m1, lst[x]);
      }
      for (int x = 0; x < n; x++) 
      {
        cin >> lst1[x];
        s2 += lst1[x];
        m2 = min(m2, lst1[x]);
      }
      cout << min(n * m1 + s2, n * m2 + s1) << "\n";
    }
    return 0;
}
