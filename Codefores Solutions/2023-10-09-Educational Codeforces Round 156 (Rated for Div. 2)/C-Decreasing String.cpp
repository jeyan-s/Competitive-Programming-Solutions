// Link to Problem Statement
// https://codeforces.com/contest/1886/problem/C

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int test; cin >> test;
    while (test--)
    {
      // int n, k, a, b; cin >> n;
      // int rslt = 0, count = 0;
      // string String; cin >> String;
      // unordered_map<int, int> Hash;
      // set<int> Set;
      // vector<pair<char, long long>> lst;
      vector<int> lst;
      stack<pair<char, int>> Stack;
      // for (int x = 0; x < n; x++) cin >> lst[x];
      string String, rslt = "", r = ""; cin >> String;
      long long n = String.length(), k = n, start = 0, N = n, pos; cin >> pos;
      // for (int x = 0; x < n; x++) lst.push_back(make_pair(String[x], x));
      // sort(lst.begin(), lst.end(), [&](pair<char, long long> x, pair<char, long long> y) 
      // {
      //   if (x.first > y.first) return true;
      //   if (x.first == y.first) return (x.second < y.second);
      //   return false;
      // });
      vector<bool> visited(n, false);
      // cout << N << " ";
      
      
      
      
      
      for (int x = 0; x < n; x++)
      {
        if (Stack.empty()) 
        {
          Stack.push(make_pair(String[x], x));
        }
        else
        {
          while (!Stack.empty() && Stack.top().first > String[x])
          {
            rslt += Stack.top().first;
            lst.push_back(Stack.top().second);
            Stack.pop();
          }
          Stack.push(make_pair(String[x], x));
        }
      }
      
      while (!Stack.empty()) 
      {
        rslt += Stack.top().first;
        lst.push_back(Stack.top().second);
        Stack.pop();
      }




      reverse(rslt.begin(), rslt.end());
      

  	  while (start + N < pos)
      {
        start += N;
        N -= 1;
        k -= 1;
        // cout << pos << " " << N << "\n";
      }
      // cout << k << " ";
      
      for (int x = 0; x + k < n; x++) visited[lst[x]] = true;
      for (int x = 0; x < n; x++) if (!visited[x]) r += String[x];
      pos -= start;
      
      // cout << r << " ";
      cout << r[pos - 1];
      // cout << "\n";
      
    }
    return 0;
}
