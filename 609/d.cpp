#include <bits/stdc++.h>

#define ll long long
#define fastio()             \
    ios::sync_with_stdio(0); \
    cin.tie(0);              \
    cout.tie(0);

using namespace std;

const int INF = -1e9;

int main()
{
    fastio();

    int n, m;
    cin >> n >> m;

    vector<vector<int>> adj(n + 1);
    vector<int> indegree(n + 1, 0);

    for (int i = 0; i < m; ++i)
    {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        indegree[b]++;
    }

    // Topological sort
    queue<int> q;
    for (int i = 1; i <= n; ++i)
    {
        if (indegree[i] == 0)
            q.push(i);
    }

    vector<int> topo;
    while (!q.empty())
    {
        int u = q.front();
        q.pop();
        topo.push_back(u);
        for (int v : adj[u])
        {
            indegree[v]--;
            if (indegree[v] == 0)
                q.push(v);
        }
    }

    vector<int> dp(n + 1, INF);
    vector<int> prev(n + 1, -1);
    dp[1] = 1;

    for (int u : topo)
    {
        for (int v : adj[u])
        {
            if (dp[u] + 1 > dp[v])
            {
                dp[v] = dp[u] + 1;
                prev[v] = u;
            }
        }
    }

    if (dp[n] < 1)
    {
        cout << "IMPOSSIBLE\n";
        return 0;
    }

    cout << dp[n] << '\n';
    vector<int> path;
    int cur = n;
    while (cur != -1)
    {
        path.push_back(cur);
        cur = prev[cur];
    }
    reverse(path.begin(), path.end());
    for (int x : path)
        cout << x << ' ';
    cout << '\n';
    return 0;
}