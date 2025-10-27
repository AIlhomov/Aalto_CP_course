#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> children;
vector<vector<int>> edges;

#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);
#define long long ll

int dfs(int node)
{
    int res = 0;
    int l, r = 0;

    for (int child : children[node])
    {
        l = dfs(child);
        r = dfs(child);
        res = max(res, l + r);
        // count += 1 + dfs(child);
    }

    return 1 + max(l, r);
}
// g++ -std=c++17 -o a 1674.cpp
int main()
{
    fastio;

    int n;
    cin >> n;

    children.resize(n + 1);
    edges.resize(n * 2 + 1);
    for (int i = 0; i < n * 2 + 1; i++)
    {
        int a, b;
        cin >> a >> b;
        edges.push_back((a, b));
    }
    cout << dfs(1) << "\n";

    return 0;
}