// Link to Problem Statement
// https://codeforces.com/contest/1864/problem/A

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int test_case; cin >> test_case;
    while (test_case--)
    {
      int n, start, end, k, minus = 1, rslt = 0; cin >> start >> end >> n;
      vector<int> lst(n), new_lst;
      k = end;
      bool Error = false;
      // for (int x = 0; x < n; x++) cin >> lst[x];
      lst[0] = start;
      lst[n - 1] = end;
      for (int x = n - 2; x > 0; x--)
      {
        k -= minus++;
        lst[x] = k;
      }
      
      for (int x = 1; x < n; x++)
      {
        if (lst[x] - lst[x - 1] <= 0) Error = true;
        new_lst.push_back(lst[x] - lst[x - 1]);
      }
      for (int x = 1; x < n - 1; x++)
      {
        if (new_lst[x] - new_lst[x - 1] >= 0) Error = true;
      }
      
      if (Error) cout << "-1\n";
      else
      {
        for (int x: lst) cout << x << ' ';
        cout << '\n';
      }
    }
    return 0;
}
