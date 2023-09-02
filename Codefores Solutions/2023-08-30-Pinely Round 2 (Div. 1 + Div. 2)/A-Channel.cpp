// Link to problem Statement
// https://codeforces.com/contest/1863/problem/A

#include <iostream>
using namespace std;

int main() 
{
    int test_case; cin >> test_case;
    while (test_case--)
    {
      int n, a, q, rslt = 0, online = 0; cin >> n >> a >> q;
      online = a;
      bool Found = a >= n;
      string s; cin >> s;
      for (char x: s)
      {
        if (x == '+')
        {
          online += 1;
          a += 1;
          // cout << '1' << ' ';
          if (a >= n) Found = true;
        }
        else a -= 1;
      }
      if (Found) 
      {
        cout << "YES";
      }
      else if (online >= n) cout << "MAYBE";
      else cout << "NO";
      cout << "\n";
    }
    return 0;
}
