// Link to Problem Statement
// https://codeforces.com/contest/1861/problem/A

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int test; cin >> test;
    while (test--)
    {
      string s; cin >> s;
      for (char x: s)
      {
        if (x == '9')
        {
          cout << 97 << '\n';
          break;
        }
        if (x == '7')
        {
          cout << 79 << '\n';
          break;
        }
      }
    }
    
    return 0;
}
