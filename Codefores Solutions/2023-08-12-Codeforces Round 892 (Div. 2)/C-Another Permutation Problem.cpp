// Link to Problem Statement
// https://codeforces.com/contest/1859/problem/C

#include <bits/stdc++.h>
using namespace std;

long long solve(vector<int> lst, int n)
{
  long long t = 0, mx = 0;
  for (int x = 0; x < n; x++)
  {
    long long tmp = ((long long) lst[x] * (x + 1));
    mx = max(mx, tmp);
    t += tmp;
  }
  return t - mx;
}

int main() 
{
    int t; cin >> t;
    
    while (t--)
    {
      int n; cin >> n;
      long long rslt = 0;
      for (int y = 0; y < n; y++)
      {
        vector<int> lst(n);
        int N = n;
        for (int x = 1; x <= y; x++)
        {
          lst[x - 1] = x;
        }
        
        for (int x = y; x < n; x++)
        {
          lst[x] = N--;
        }
        rslt = max(rslt, solve(lst, n));
      }
      
        cout << rslt << '\n';
    }
    
    return 0;
}
