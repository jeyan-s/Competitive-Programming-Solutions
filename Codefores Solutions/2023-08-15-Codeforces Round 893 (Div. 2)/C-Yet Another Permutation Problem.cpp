// Link to Problem Statement
// https://codeforces.com/contest/1858/problem/B

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int t; cin >> t;
    while (t--)
    {
      
      int n; cin >> n;
      vector<int> rslt, visited(n + 1, 0);
      
      for (int x = 1; x <= n; x++)
      {
        int tmp = x;
        while (tmp <= n)
        {
          if (visited[tmp] == 0) rslt.push_back(tmp);
          visited[tmp] = 1;
          tmp *= 2;
        }
      }
      
      for (int x: rslt) cout << x << ' ';
      cout << '\n';
      
    }
    return 0;
}

//999999999
