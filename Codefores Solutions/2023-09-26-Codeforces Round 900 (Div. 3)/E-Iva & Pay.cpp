// Link to Problem Statement
// https://codeforces.com/contest/1878/problem/E

#include <bits/stdc++.h>
using namespace std;

int solve(vector<vector<int>> &lst, int &left, int &right)
{
  int rslt = 0, y = 0;
  if (left != 0)
    for (int x = 31; x >= 0; x--)
    {
      if (lst[right][x] - lst[left - 1][x] == 0)
        rslt += pow(2, y);
      y += 1;
    }
  else
    for (int x = 31; x >= 0; x--)
    {
      if (lst[right][x] == 0)
        rslt += pow(2, y);
      y += 1;
    }
  return rslt;
}


int main() 
{
    int test; cin >> test;
    while (test--)
    {
      int n; cin >> n;
      vector<int> lst(n);
      for (int x = 0; x < n; x++) cin >> lst[x];
      vector<vector<int>> bits(n, vector<int>(32, 0)), prefix(n, vector<int>(32, 0));
      
      for (int x = 0; x < n; x++)
      {
        int tmp = lst[x];
        int y = 31;
        while (tmp)
        {
          bits[x][y] = tmp & 1;
          tmp >>= 1;
          y -= 1;
        }
      }
      
      // for (int x = 0; x < n; x++)
      // {
      //   for (int y = 0; y < 32; y++)
      //   {
      //     cout << bits[x][y] << " ";
      //   }
      //   cout << "\n";
      // }
      
      for (int x = 0; x < n; x++)
      {
        for (int y = 0; y < 32; y++)
        {
          if (x - 1 >= 0)
            prefix[x][y] = prefix[x - 1][y];
          prefix[x][y] += int(bits[x][y] == 0);
        }
      }
      
      int q; cin >> q;
      
      for (int __ = 0; __ < q; __++)
      {
        int l, k; cin >> l >> k;
        int low = l - 1;
        int high = n - 1;
        int rslt = -1;
        bool Found = false;
        l -= 1;
        while (low <= high)
        {
          int mid = low + (high - low) / 2;
          // cout << low << " " << mid << " " << high << "\n";
          int sl = solve(prefix, l, mid);
          // int sl = 10;
          if (sl >= k)
          {
            rslt = mid; 
            Found = true;
            low = mid + 1;
          }
          else
          {
            high = mid - 1;
          }
        }
          if (Found) cout << rslt + 1 << ' ';
          else cout << -1 << ' ';

      }
      cout << "\n";
      }
    return 0;
}
