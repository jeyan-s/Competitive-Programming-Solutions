// Link to Problem Statement
// https://codeforces.com/contest/1860/problem/A

#include <bits/stdc++.h>
using namespace std;

int main() 
{
  
    int test_case; cin >> test_case;
    while (test_case--)
    {
      string str, s1 = "", s2 = ""; cin >> str;
      int n = str.length();
      for (int x = 0; x < n; x++) s1 += '(';
      for (int x = 0; x < n; x++) s1 += ')';
      for (int x = 0; x < 2 * n; x++)
      {
        if (x & 1) s2 += ')';
        else s2 += '(';
      }
      if (s2.find(str) == string::npos)
      {
        cout << "YES\n" << s2 << '\n';
      }
      else if (s1.find(str) == string::npos)
      {
        cout << "YES\n" << s1 << '\n';
      }
      else cout << "NO\n";
    }
    
    return 0;
}
