#include <bits/stdc++.h>
using namespace std;

#define fastio()             \
    ios::sync_with_stdio(0); \
    cin.tie(0);              \
    cout.tie(0);

typedef long long ll;
const ll INF = 1e18;
const int MOD = 1e9 + 7;

int main()
{
    fastio();

    int n, m;
    cin >> n >> m;
    vector<vector<pair<int, ll>>> g(n + 1);
    for (int i = 0; i < m; ++i)
    {
        int a, b;
        ll c;
        cin >> a >> b >> c;
        g[a].emplace_back(b, c);
    }

    vector<ll> dist(n + 1, INF);
    vector<ll> ways(n + 1, 0);
    vector<int> min_flights(n + 1, INT_MAX);
    vector<int> max_flights(n + 1, 0);

    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<>> pq;
    dist[1] = 0;
    ways[1] = 1;
    min_flights[1] = 0;
    max_flights[1] = 0;
    pq.emplace(0, 1);

    while (!pq.empty())
    {
        auto [d, u] = pq.top();
        pq.pop();
        if (d > dist[u])
            continue;
        for (auto [v, w] : g[u])
        {
            if (dist[v] > dist[u] + w)
            {
                dist[v] = dist[u] + w;
                ways[v] = ways[u];
                min_flights[v] = min_flights[u] + 1;
                max_flights[v] = max_flights[u] + 1;
                pq.emplace(dist[v], v);
            }
            else if (dist[v] == dist[u] + w)
            {
                ways[v] = (ways[v] + ways[u]) % MOD;
                min_flights[v] = min(min_flights[v], min_flights[u] + 1);
                max_flights[v] = max(max_flights[v], max_flights[u] + 1);
            }
        }
    }

    cout << dist[n] << " " << ways[n] << " " << min_flights[n] << " " << max_flights[n] << "\n";
    return 0;
}