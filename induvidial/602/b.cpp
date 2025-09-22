// g++ -std=c++17 -O2 -pipe -Wall -Wextra a.cpp -o a
#include <bits/stdc++.h>
using namespace std;

struct FenwickTree2D
{
    int n, m;
    vector<vector<int>> bit; // 0-based BIT

    FenwickTree2D(int n = 0, int m = 0) { init(n, m); }

    void init(int nn, int mm)
    {
        n = nn;
        m = mm;
        bit.assign(n, vector<int>(m, 0));
    }

    void add(int x, int y, int delta)
    {
        for (int i = x; i < n; i = (i | (i + 1)))
            for (int j = y; j < m; j = (j | (j + 1)))
                bit[i][j] += delta;
    }

    int sum(int x, int y) const
    {
        int ret = 0;
        for (int i = x; i >= 0; i = ((i & (i + 1)) - 1))
            for (int j = y; j >= 0; j = ((j & (j + 1)) - 1))
                ret += bit[i][j];
        return ret;
    }

    int rect(int x1, int y1, int x2, int y2) const
    {
        if (x1 > x2 || y1 > y2)
            return 0;
        return sum(x2, y2) - (x1 ? sum(x1 - 1, y2) : 0) - (y1 ? sum(x2, y1 - 1) : 0) + ((x1 && y1) ? sum(x1 - 1, y1 - 1) : 0);
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;
    vector<string> g(n);
    for (int i = 0; i < n; ++i)
        cin >> g[i];

    FenwickTree2D ft(n, n);

    for (int y = 0; y < n; ++y)
    {
        for (int x = 0; x < n; ++x)
        {
            if (g[y][x] == '*')
                ft.add(y, x, 1);
        }
    }

    while (q--)
    {
        int y1, x1, y2, x2;
        cin >> y1 >> x1 >> y2 >> x2;

        --y1;
        --x1;
        --y2;
        --x2;
        cout << ft.rect(y1, x1, y2, x2) << '\n';
    }
    return 0;
}
