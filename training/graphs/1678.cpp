#include <bits/stdc++.h>
using namespace std;
#define fastio()             \
    ios::sync_with_stdio(0); \
    cin.tie(0);              \
    cout.tie(0);

vector<vector<int>> adj;
vector<int> parent, state;
int cycle_start = -1, cycle_end = -1;

bool dfs(int start, int n)
{
    stack<int> st;
    st.push(start);
    while (!st.empty())
    {
        int node = st.top();
        if (state[node] == 0)
        {
            state[node] = 1; // visiting
            for (int neighbor : adj[node])
            {
                if (state[neighbor] == 0)
                {
                    parent[neighbor] = node;
                    st.push(neighbor);
                }
                else if (state[neighbor] == 1)
                {
                    cycle_start = neighbor;
                    cycle_end = node;
                    return true;
                }
            }
        }
        else
        {
            state[node] = 2; // visited
            st.pop();
        }
    }
    return false;
}

int main()
{
    fastio();
    int n, m;
    cin >> n >> m;
    adj.resize(n + 1);
    parent.resize(n + 1, -1);
    state.resize(n + 1, 0);

    for (int i = 0; i < m; i++)
    {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
    }

    for (int i = 1; i <= n; i++)
    {
        if (state[i] == 0)
        {
            if (dfs(i, n))
                break;
        }
    }

    if (cycle_start == -1)
    {
        cout << "IMPOSSIBLE\n";
    }
    else
    {
        vector<int> cycle;
        cycle.push_back(cycle_start);
        for (int v = cycle_end; v != cycle_start; v = parent[v])
            cycle.push_back(v);
        cycle.push_back(cycle_start);
        reverse(cycle.begin(), cycle.end());
        cout << cycle.size() << "\n";
        for (int v : cycle)
            cout << v << " ";
        cout << "\n";
    }
    return 0;
}
