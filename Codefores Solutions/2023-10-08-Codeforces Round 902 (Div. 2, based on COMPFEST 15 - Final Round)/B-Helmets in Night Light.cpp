// Link to Problem Statement
// https://codeforces.com/contest/1877/problem/B

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int test; cin >> test;
    while (test--)
    {
      long long  n, K, a, b; cin >> n >> K;
      long long  rslt = 0, count = 0;
      set<long long> Set;
      // string String; cin >> String;
      //unordered_
      map<long long, long long> Hash;
      vector<pair<long long, long long>> lst;
      vector<int>  lst1(n), lst2(n);
      for (int x = 0; x < n; x++)  cin >> lst1[x];
      for (int x = 0; x < n; x++)  cin >> lst2[x];
      for (int x = 0; x < n; x++) 
      {
        a = lst1[x]; b = lst2[x];
        lst.push_back(make_pair(a, b));
      }
      
      sort(lst.begin(), lst.end(), [&](pair<long long, long long> x, pair<long long, long long> y) 
      {
        if (x.second < y.second) return true;
        if (x.second == y.second) 
        {
          if (x.first > y.first) return true;
          else return false;
        }
        return false;
      });
      
      rslt += K;
      int k = min(lst[0].second, K);
      Set.insert(k);
      Hash[lst[0].second] = lst[0].first;
      
      for (int x = 1; x < n; x++)
      {
        long long cost = *Set.begin();
        if (cost > K)
        {
          rslt += K;
          continue;
        }
        rslt += cost;
        Hash[cost] -= 1;
        Hash[lst[x].second] += lst[x].first;
        if (Hash[cost] == 0) Set.erase(cost);
        Set.insert(lst[x].second);
        // cout << lst[x].first << " " << lst[x].second << "\n";
      }
      cout << rslt << "\n";
    }
    return 0;
}
