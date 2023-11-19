// Link to Problem Statement
// https://codeforces.com/contest/1881/problem/D

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int test; cin >> test;
    while (test--)
    {
      long long n, t, d; cin >> n;
      unordered_map<long long, long long> Hash;
      // vector<long long> lst(n);
      bool Error = false;
      for (int x = 0; x < n; x++) 
      {
        d = 2;
        cin >> t;
        while (d * d <= t)
        {
          while (t % d == 0)
          {
            t /= d;
            Hash[d] += 1;
          }
          d += 1;
        }
        if (t != 1) Hash[t] += 1;
      }
      for (pair<long long, long long> x: Hash)
      {
        if (x.first == 1) continue;
        if (x.second % n != 0) Error = true;
      }
      if (Error) cout << "NO";
      else cout << "YES";
      cout << "\n";
    }
    return 0;
}
