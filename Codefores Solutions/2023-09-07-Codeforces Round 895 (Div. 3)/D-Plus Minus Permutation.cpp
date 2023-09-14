// Link to Problem Statement
// https://codeforces.com/contest/1872/problem/D

#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int test; cin >> test;
    while (test--)
    {
      int n, a, b; cin >> n >> a >> b;
      long long lcm = ((long long) a * b) / __gcd(a, b), lost = n / lcm, x = 0, y = 0;
      a = (n / a) - lost; b = (n / b) - lost;
      x = ((long long) b * (b + 1)) / 2;
      long long k = n - a;
      y = ((long long) k * (k + 1)) / 2;
      y = (((long long) n * (n + 1)) / 2) - y;
      long long rslt = y - x;
      cout << rslt << "\n";
      // cout << a << ' ' << b << '\n'; 
    }
    return 0;
}
