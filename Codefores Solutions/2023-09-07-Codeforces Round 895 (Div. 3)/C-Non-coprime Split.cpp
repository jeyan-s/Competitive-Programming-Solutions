// Link to Problem Statement
// https://codeforces.com/contest/1872/problem/C

#include <bits/stdc++.h>
using namespace std;

bool prime(int n)
{
  int x = 2; 
  while (x * x <= n)
  {
    if (n % x == 0 && (n - x) % x == 0)
    {
      cout << x << " " << (n - x);
      return true;
    }
    x++;
  }
  return false;
}

int main() 
{
    int test; cin >> test;
    while (test--)
    {
      int l, r; cin >> l >> r;
      bool Found = false;
      
      if (l == r)
      {
        if (l & 1)
        {
          Found = prime(l);
        }
        else
        {
          if (__gcd(l / 2, l / 2) != 1)
          {
            cout << l / 2 << " " << l / 2;
            Found = true;
          }
        }
      }
      else
      {
        if (r & 1)
        {
          if (__gcd((r - 1) / 2, (r - 1) / 2) != 1)
          {
            cout << (r - 1) / 2 << " " << (r - 1) / 2;
            Found = true;
          }
        }
        else
        {
          if (__gcd(r / 2, r / 2) != 1)
          {
            cout << (r / 2) << " " << (r / 2);
            Found = true;
          }
        }
      }

      if (!Found) cout << "-1";
      cout << "\n";
    }
    return 0;
}
