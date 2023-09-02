// Link to Problem Statement
// https://codeforces.com/contest/1861/problem/B

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int test; cin >> test;
    while (test--)
    {
      string s1, s2; cin >> s1 >> s2;
      int n = s1.length();
      bool Found = false;
      for (int x = 0; x < n - 1; x++)
      {
        if (s1[x] == '0' && s2[x] == '0' && s1[x + 1] == '1' && s2[x + 1] == '1')
        {
          Found = true;
          break;
        }
      }
      if (Found) cout << "YES\n";
      else cout << "NO\n";
    }
    
    return 0;
}
