// Link to Problem Statement
// https://codeforces.com/contest/1862/problem/B

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int test_cases; cin >> test_cases;
    
    while (test_cases--)
    {
      int n; cin >> n;
      vector<int> lst(n), rslt;
      for (int x = 0; x < n; x++) cin >> lst[x];
      rslt.push_back(lst[0]);
      int k = 1;
      for (int x = 1; x < n; x++)
      {
        if (lst[x] >= rslt[k - 1])
        {
          rslt.push_back(lst[x]);
          k++;
        }
        else 
        {
          rslt.push_back(1);
          rslt.push_back(lst[x]);
          k += 2;
        }
      }
      cout << (int) rslt.size() << '\n';
      for (int x: rslt) cout << x << ' ';
      cout << '\n';
    }
    
    return 0;
}
