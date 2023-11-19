// Link to Problem Statement
// https://codeforces.com/contest/1882/problem/B

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int test; cin >> test;
    while (test--)
    {
      
      int n, k, a, b, y = 1, rslt = 0, cnt = 0; cin >> n;
      unordered_map<int, vector<int>> Hash;
      unordered_map<int, int> Hash1;
      vector<vector<int>> lst;
      
      for (int x = 0; x < n; x++) 
      {
        vector<int> tmp;
        int k; cin >> k;
        for (int y = 0; y < k; y++) 
        {
          int t; cin >> t;
          tmp.push_back(t);
          Hash[t].push_back(x);
          Hash1[t] += 1;
        }
        lst.push_back(tmp);
      }
      
      
      k = Hash1.size();
      for (int x = 1; x < 51; x++)
      {
        cnt = k;
        for (int idx: Hash[x])
        {
          for (int y: lst[idx]) 
          {
            Hash1[y] -= 1;
            if (Hash1[y] == 0) cnt -= 1;
          }
        }
        if (cnt != k) rslt = max(rslt, cnt);
        for (int idx: Hash[x])
        {
          for (int y: lst[idx]) 
          {
            Hash1[y] += 1;
          }
        }
      }
      
      // for (pair<int, int> x: Hash1) cout << x.first << " " << x.second << "\n";
      
      cout << rslt << "\n";
    }
    return 0;
}
