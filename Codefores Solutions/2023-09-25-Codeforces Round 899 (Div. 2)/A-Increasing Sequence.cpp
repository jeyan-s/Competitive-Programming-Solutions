// Link to Problem Statement
// https://codeforces.com/contest/1882/problem/A

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int test; cin >> test;
    while (test--)
    {
      int n, k, a, b, y = 1; cin >> n;
      // unordered_map<int, int> Hash;
      // string String; cin >> String;
      vector<int> lst(n), rslt(n, -1);
      for (int x = 0; x < n; x++) cin >> lst[x];
      for (int x = 0; x < n; x++)
      {
        if (lst[x] == y) rslt[x] = ++y;
        else rslt[x] = y;
        y++;
      }
      // for (int x = 0; x < n; x++) cout << rslt[x] << " ";
      cout << rslt[n - 1] << "\n";
    }
    return 0;
}
