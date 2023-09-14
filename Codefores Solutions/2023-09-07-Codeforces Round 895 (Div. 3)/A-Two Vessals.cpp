#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int test; cin >> test;
    while (test--)
    {
      int a, b, c; cin >> a >> b >> c;
      int diff = ceil(abs(b - a) / 2.0);
      cout << ceil(diff / (float) c) << "\n";
    }
    return 0;
}
