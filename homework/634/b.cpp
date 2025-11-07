#include <bits/stdc++.h>
using namespace std;

#define fastio               \
    ios::sync_with_stdio(0); \
    cin.tie(0);              \
    cout.tie(0);

// g++ b.cpp -o b -std=c++17
int main()
{
    fastio;

    int n;
    if (!(cin >> n))
        return 0;
    unordered_set<long long> ys, xs;
    ys.reserve(n * 2);
    xs.reserve(n * 2);
    ys.max_load_factor(0.7);
    xs.max_load_factor(0.7);

    for (int i = 0; i < n; ++i)
    {
        long long x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        if (y1 == y2)
        {
            ys.insert(y1); // horizontal line: y = constant
        }
        else if (x1 == x2)
        {
            xs.insert(x1); // vertical line: x = constant
        }
    }

    long long H = (long long)ys.size();
    long long V = (long long)xs.size();
    cout << H * V << "\n";
    return 0;
}
