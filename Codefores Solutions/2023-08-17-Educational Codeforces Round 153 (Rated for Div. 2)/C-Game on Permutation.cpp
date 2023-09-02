// Link to Problem Statement
// https://codeforces.com/contest/1860/problem/C

#include <bits/stdc++.h>
using namespace std;

int main() 
{
  
    int test_case; cin >> test_case;
    while (test_case--)
    {
      int n, first = (int) 1e7, second = (int) 1e7; cin >> n;
      vector<int> lst(n), rslt(n, 1);
      set<int> Set;
      for (int x = 0; x < n; x++) cin >> lst[x];
      
      for (int x = 0; x < n; x++)
      {
        if (lst[x] < first)
        {
          first = lst[x];
          rslt[x] = 0;
        }
        else if (lst[x] > second)
        {
          rslt[x] = 0;
        }
        else if (lst[x] < second)
        {
          second = lst[x];
        }
      }
      cout << (int)accumulate(rslt.begin(), rslt.end(), 0) << '\n';
    }
    
    return 0;
}
