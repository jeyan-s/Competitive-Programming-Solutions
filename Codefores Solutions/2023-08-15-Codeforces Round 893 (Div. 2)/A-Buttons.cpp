// Link to Problem Statement
// https://codeforces.com/contest/1858/problem/A

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int t; cin >> t;
    while (t--)
    {
      
      int a, b, c; cin >> a >> b >> c;
      if (c & 1)
      {
        if (b > a) cout << "Second";
        else cout << "First";
      }
      else
      {
        if (a > b) cout << "First";
        else cout << "Second";
      }
      cout << '\n';
      
    }
    return 0;
}
