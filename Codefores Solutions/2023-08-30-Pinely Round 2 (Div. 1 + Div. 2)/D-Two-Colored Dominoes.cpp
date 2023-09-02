// Link to problem Statement
// https://codeforces.com/contest/1863/problem/D

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int test_case; cin >> test_case;
    while (test_case--)
    {
      int n, m; cin >> n >> m;
      vector<string> lst(n), rslt(n);
      string tmp = "";
      bool Error = false;
      
      for (int x = 0; x < m; x++) tmp += ".";
      for (int x = 0; x < n; x++) 
      {
        cin >> lst[x];
        rslt[x] = tmp;
      }
      
      for (int x = 0; x < n; x++)
      {
        char prev = 'W';
        for (int y = 0; y < m; y++)
        {
          if (lst[x][y] == 'U')
          {
            if (prev == 'B')
            {
              rslt[x][y] = 'W';
              rslt[x + 1][y] = 'B';
              prev = 'W';
            }
            else
            {
              rslt[x][y] = 'B';
              rslt[x + 1][y] = 'W';
              prev = 'B';
            }
          }
        }
      }
      
      for (int y = 0; y < m; y++)
      {
        char prev = 'W';
        for (int x = 0; x < n; x++)
        {
          if (lst[x][y] == 'L')
          {
            if (prev == 'B')
            {
              rslt[x][y] = 'W';
              rslt[x][y + 1] = 'B';
              prev = 'W';
            }
            else
            {
              rslt[x][y] = 'B';
              rslt[x][y + 1] = 'W';
              prev = 'B';
            }
          }
        }
      }
      
      vector<int> col(m), row(n);
      for (int x = 0; x < n; x++)
      {
        for (int y = 0; y < m; y++)
        {
          if (rslt[x][y] == 'B') 
          {
            row[x]++;
            col[y]++;
          }
          else if (rslt[x][y] == 'W')
          {
            row[x]--;
            col[y]--;
          }
        }
      }
      
      for (int x = 0; x < n; x++) if (row[x] != 0) Error = true;
      for (int x = 0; x < m; x++) if (col[x] != 0) Error = true;
      
      if (Error) cout << -1 << '\n';
      else
      {
        for (int x = 0; x < n; x++)
        cout << rslt[x] << "\n";
      }
    }
    return 0;
}
