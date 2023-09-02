// Link to Problem Statement
// https://codeforces.com/contest/1864/problem/B

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int test_case; cin >> test_case;
    while (test_case--)
    {
      int n, k; cin >> n >> k;
      string str, rslt = "";
      cin >> str;
      
      vector<char> Odd, Even, Whole;
      if (k & 1)
      {
        int E = 0, O = 0;
        for (int x = 0; x < n; x++)
        {
          if (x & 1) Odd.push_back(str[x]);
          else Even.push_back(str[x]);
        }
        sort(Odd.begin(), Odd.end());
        sort(Even.begin(), Even.end());
        for (int x = 0; x < n; x++)
        {
          if (x & 1) rslt += Odd[O++];
          else rslt += Even[E++];
        }
      }
      else
      {
        sort(str.begin(), str.end());
        rslt = str;
      }
      cout << rslt << '\n';
    }
    return 0;
}
