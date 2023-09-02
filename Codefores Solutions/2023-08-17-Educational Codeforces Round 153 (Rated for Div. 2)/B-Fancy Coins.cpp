// Link to Problem Statement
// https://codeforces.com/contest/1860/problem/B

#include <bits/stdc++.h>
using namespace std;

int main() 
{
  
    int test_case; cin >> test_case;
    while (test_case--)
    {
      long long n, k, one, ak, rslt; cin >> n >> k >> one >> ak;
      if (n % k <= one) 
      {
        one -= (n % k);
        n -= (n % k);
      }
      n -= (one / k) * k;
      one -= (one / k) * k;
      long long p = n / k, rem = n % k;
      p -= min(p, ak);
      n = p * k + rem;
      rslt = (n / k) + (n % k);
      n -= min(n, one);
      rslt = min(rslt, (n / k) + (n % k));
      cout << rslt << '\n';
    }
    
    return 0;
}
