// Link to Problem Statement
// https://codeforces.com/contest/1878/problem/C

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int test; cin >> test;
    while (test--)
    {
      long long n, k, x; cin >> n >> k >> x;
      long long left = (k * (k + 1)) / 2;
      long long new_k = n - k;
      long long right = (new_k * (new_k + 1)) / 2;
      right = ((n * (n + 1)) / 2) - right;
      if (x >= left && x <= right)
        cout << "YES\n";
      else
        cout << "NO\n";
    }
    return 0;
}
