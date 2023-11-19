// Link to Problem Statement
// https://codeforces.com/contest/1878/problem/A

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int test; cin >> test;
    while (test--)
    {
      int n, k, a, b, rslt = 0, cnt = 0; cin >> n >> k; 
      vector<int> lst(n);
      for (int x = 0; x < n; x++) cin >> lst[x];
      // string String; cin >> String;
      // unordered_map<int, int> Hash;
      bool Found = false, Error = false;
      for (int x = 0; x < n; x++)
      {
        if (lst[x] == k) Found = true;
      }
      if (Found) cout << "YES\n";
      else cout << "NO\n";
    }
    return 0;
}
