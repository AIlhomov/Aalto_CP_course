// g++ -std=c++17 -O2 -pipe -Wall -Wextra a.cpp -o a
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1'000'000'007;
const int INF = 1e9;
#define ll long long
#define fast                     \
    ios::sync_with_stdio(false); \
    cin.tie(nullptr);

vector<ll> solve(vector<ll> &arr, vector<vector<ll>> &queries, ll n, ll q)
{
    vector<ll> prefixSum(n + 1, 0);
    for (int i = 1; i <= n; i++)
    {
        prefixSum[i] = prefixSum[i - 1] + arr[i - 1];
    }
    vector<ll> res;
    for (auto &query : queries)
    {
        ll l = query[0], r = query[1];
        ll sum = prefixSum[r] - prefixSum[l - 1];
        res.push_back(sum);
    }
    return res;
}

int main()
{
    fast;

    ll n, q;
    cin >> n >> q;
    vector<ll> a;
    int x;
    for (int i = 0; i < n; i++)
    {
        cin >> x;
        a.push_back(x);
    }
    vector<vector<ll>> ab;
    int l, r;
    for (int i = 0; i < q; i++)
    {
        cin >> l >> r;
        ab.push_back({l, r});
    }
    vector<ll> ans = solve(a, ab, n, q);
    for (ll val : ans)
    {
        cout << val << '\n';
    }

    return 0;
}