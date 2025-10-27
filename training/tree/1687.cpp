#include <bits/stdc++.h>
using namespace std;

#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);
#define long long ll

// g++ -std=c++17 -o a 1687.cpp
int main()
{
    fastio;

    int n, q;
    cin >> n >> q;

    // Binary lifting preprocessing
    // LOG = ceil(log2(n))
    int LOG = 20;

    vector<vector<int>> up(n + 1, vector<int>(LOG, -1));

    up[1][0] = -1;
    for (int i = 2; i <= n; i++)
    {
        cin >> up[i][0];
    }

    // LCA table
    for (int j = 1; j < LOG; j++)
    {
        for (int i = 1; i <= n; i++)
        {
            if (up[i][j - 1] != -1)
            {
                up[i][j] = up[up[i][j - 1]][j - 1];
            }
        }
    }

    for (int i = 0; i < q; i++)
    {
        int x, k;
        cin >> x >> k;

        int current = x;
        for (int j = 0; j < LOG; j++)
        {
            if (k & (1 << j))
            {
                current = up[current][j];
                if (current == -1)
                    break;
            }
        }

        cout << current << "\n";
    }

    return 0;
}