#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define fastio()             \
    ios::sync_with_stdio(0); \
    cin.tie(0);              \
    cout.tie(0);

#define MOD 1'000'000'007
// g++ -std=c++17 -O2 -pipe -Wall -Wextra hotels.cpp -o hotels
int main()
{
    fastio();
    int n, m;
    cin >> n >> m;

    vector<vector<int>> adj(n);
    vector<int> indegree(n, 0);
    for (int i = 0; i < m; ++i)
    {
        int a, b;
        cin >> a >> b;
        --a;
        --b;
        adj[a].push_back(b);
        indegree[b]++;
    }

    // Topological sort (Kahn's algorithm)
    queue<int> q;
    for (int i = 0; i < n; ++i)
        if (indegree[i] == 0)
            q.push(i);

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

    // DP: number of ways to reach each node from node 0
    vector<ll> dp(n, 0);
    dp[0] = 1;
    for (int u : topo)
    {
        for (int v : adj[u])
        {
            dp[v] = (dp[v] + dp[u]) % MOD;
        }
    }

    cout << dp[n - 1] << '\n';

    return 0;
}