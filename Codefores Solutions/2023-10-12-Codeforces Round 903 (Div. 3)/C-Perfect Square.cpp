// Link to Problem Statement
// https://codeforces.com/contest/1881/problem/C

#include<bits/stdc++.h>
using namespace std;
vector<string> solve(vector<string> mat, int n)
{
   for(int i=0; i<n; i++)
   {
     for(int j=i+1; j<n; j++)
         swap(mat[i][j], mat[j][i]);
    }

   //Reversing each row of the matrix
   for(int i=0; i<n; i++)
   {
     for(int j=0; j<n/2; j++)
        swap(mat[i][j], mat[i][n-j-1]);
   }

   return mat;
}

int main() 
{
    int test; cin >> test;
    while (test--)
    {
      int n; cin >> n;
      vector<string> lst(n);
      
      unordered_map<char, int> Hash;
      for (int x = 0; x < n; x++) cin >> lst[x];
      vector<string> one, two, three;
      one = solve(lst, n);
      two = solve(one, n);
      three = solve(two, n);
      vector<vector<int>> rslt(n, vector<int>(n, 10000));
      for (int c = 97; c < 97 + 26; c++)
      {
        char C = char(c);
        for (int x = 0; x < n / 2; x++)
        {
          for (int y = 0; y < n / 2; y++)
          {
            char a = lst[x][y], b = one[x][y], c_ = two[x][y], d = three[x][y];
            if (C < a || C < b || C < c_ || C < d) continue;
            int cnt = (C - a) + (C - b) + (C - c_) + (C - d);
            rslt[x][y] = min(rslt[x][y], cnt);
          }
        }
      }
      int r = 0;
      for (int x = 0; x < n / 2; x++)
      {
        for (int y = 0; y < n / 2; y++)
        {
          r += rslt[x][y];
        }
      }
      cout << r << "\n";
    }
    return 0;
}
