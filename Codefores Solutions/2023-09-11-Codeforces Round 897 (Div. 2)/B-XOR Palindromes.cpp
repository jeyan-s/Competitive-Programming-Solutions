// Link to Problem Statement
// https://codeforces.com/contest/1867/problem/B

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int test_case; cin >> test_case;
    while (test_case--)
    {
      int n, k, a, b, Oper = 0; cin >> n;
      string String, rslt = ""; cin >> String;
      vector<int> lst;
      for (int x = 0; x <= n; x++) rslt += "0";
      
      for (int x = 0; x < n / 2; x++)
      {
        if (String[x] != String[n - x - 1])
        {
          Oper += 1;
        }
      }
      lst.push_back(Oper);
      
      for (int x = 0; x < n / 2; x++)
      {
        if (String[x] == String[n - x - 1])
        {
          Oper += 2;
          lst.push_back(Oper);
        }
      }
      
      // for (int x: lst) cout << x << " ";
      // cout << "\n";
      
      for (int x: lst)
      {
        rslt[x] = '1';
        if ((n & 1) && (x + 1 <= n)) rslt[x + 1] = '1';
      }
      
      cout << rslt << "\n";
      
    }
    return 0;
}
