// Link to Problem Statement
// https://codeforces.com/contest/1867/problem/A

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int test_case; cin >> test_case;
    while (test_case--)
    {
      int n, k, a, b; cin >> n;
      vector<int> lst(n), rslt(n);
      vector<pair<int, int>> need;
      for (int x = 0; x < n; x++) cin >> lst[x];
      for (int x = 0; x < n; x++)
      {
        need.push_back({lst[x], x});
      }
      sort(need.begin(), need.end());
      int y = n;
      for (pair<int, int> x: need)
      {
        rslt[x.second] = y--;
      }
      for (int x = 0; x < n; x++) cout << rslt[x] << " ";
      cout << "\n";
    }
    return 0;
}
