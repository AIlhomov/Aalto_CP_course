#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> children;
vector<int> subordinates;
#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);
#define long long ll

int dfs(int node)
{
    int count = 0;

    for (int child : children[node])
    {
        count += 1 + dfs(child);
    }

    subordinates[node] = count;
    return count;
}
// g++ -std=c++17 -o a 1674.cpp
int main()
{
    fastio;

    int n;
    cin >> n;

    children.resize(n + 1);
    subordinates.resize(n + 1);

    for (int i = 2; i <= n; i++)
    {
        int boss;
        cin >> boss;
        children[boss].push_back(i);
    }

    dfs(1);

    for (int i = 1; i <= n; i++)
    {
        cout << subordinates[i];
        if (i < n)
            cout << " ";
    }
    cout << "\n";

    return 0;
}