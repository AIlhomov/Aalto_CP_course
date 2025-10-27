#include <bits/stdc++.h>

using namespace std;
#define ll long long

#define fastio()                  \
    ios_base::sync_with_stdio(0); \
    cin.tie(0);                   \
    cout.tie(0);

const int MAXN = 200005;
const int LOG = 20;

vector<int> adj[MAXN];
int up[MAXN][LOG];
int depth[MAXN];

void dfs(int v, int parent)
{
    up[v][0] = parent;
    for (int i = 1; i < LOG; i++)
    {
        if (up[v][i - 1] != -1)
            up[v][i] = up[up[v][i - 1]][i - 1];
        else
            up[v][i] = -1;
    }

    for (int child : adj[v])
    {
        if (child != parent)
        {
            depth[child] = depth[v] + 1;
            dfs(child, v);
        }
    }
}

int lca(int a, int b)
{
    if (depth[a] < depth[b])
        swap(a, b);

    // Bring a to the same level as b
    int diff = depth[a] - depth[b];
    for (int i = 0; i < LOG; i++)
    {
        if ((diff >> i) & 1)
        {
            a = up[a][i];
        }
    }

    if (a == b)
        return a;

    // Binary search for LCA
    for (int i = LOG - 1; i >= 0; i--)
    {
        if (up[a][i] != up[b][i])
        {
            a = up[a][i];
            b = up[b][i];
        }
    }

    return up[a][0];
}

// g++ -std=c++17 -O2 -pipe -Wall -Wextra a.cpp -o a
int main()
{
    fastio();

    int n, q;
    cin >> n >> q;

    for (int i = 2; i <= n; i++)
    {
        int parent;
        cin >> parent;
        adj[parent].push_back(i);
        adj[i].push_back(parent);
    }

    depth[1] = 0;
    dfs(1, -1);

    while (q--)
    {
        int a, b;
        cin >> a >> b;
        cout << lca(a, b) << "\n";
    }

    return 0;
}