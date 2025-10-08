#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define fastio()             \
    ios::sync_with_stdio(0); \
    cin.tie(0);              \
    cout.tie(0);
#define INF 1e18
#define MOD 1000000007

bool bfs(const vector<vector<ll>> &rGraph, int s, int t, vector<int> &parent)
{

    int V = rGraph.size();
    vector<bool> visited(V, false);

    queue<int> q;
    q.push(s);
    visited[s] = true;
    parent[s] = -1;

    while (!q.empty())
    {
        int u = q.front();
        q.pop();

        for (int v = 0; v < V; v++)
        {
            if (!visited[v] && rGraph[u][v] > 0)
            {

                if (v == t)
                {
                    parent[v] = u;
                    return true;
                }
                q.push(v);
                parent[v] = u;
                visited[v] = true;
            }
        }
    }

    return false;
}

ll ford_fulkerson(vector<vector<ll>> graph, int s, int t)
{
    int V = graph.size();
    vector<vector<ll>> rGraph = graph;
    vector<int> parent(V);

    ll max_flow = 0;

    while (bfs(rGraph, s, t, parent))
    {
        ll path_flow = INF;
        for (int v = t; v != s; v = parent[v])
        {
            int u = parent[v];
            path_flow = min(path_flow, rGraph[u][v]);
        }

        for (int v = t; v != s; v = parent[v])
        {
            int u = parent[v];
            rGraph[u][v] -= path_flow;
            rGraph[v][u] += path_flow;
        }

        max_flow += path_flow;
    }

    return max_flow;
}

int main()
{
    fastio();

    int n, m;
    cin >> n >> m;
    int source = 0;
    int sink = n - 1;
    vector<vector<ll>> graph(n, vector<ll>(n, 0));

    for (int i = 0; i < m; i++)
    {
        int a, b;
        ll c;
        cin >> a >> b >> c;
        graph[a - 1][b - 1] += c;
    }

    ll max_flow = ford_fulkerson(graph, source, sink);
    cout << max_flow << "\n";

    return 0;
}