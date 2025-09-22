// g++ -std=c++17 -O2 -pipe -Wall -Wextra a.cpp -o a
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1'000'000'007;
const int INF = 1e9;
#define ll long long
#define fast                     \
    ios::sync_with_stdio(false); \
    cin.tie(nullptr);

int main()
{
    fast;

    ll n, q;
    cin >> n >> q;
    vector<ll> prefixX(n + 1, 0);
    ll x;

    for (int i = 1; i <= n; i++)
    {
        cin >> x;
        prefixX[i] = prefixX[i - 1] ^ x;
    }
    ll l, r;
    while (q--)
    {
        cin >> l >> r;
        cout << (prefixX[r] ^ prefixX[l - 1]) << '\n';
    }

    return 0;
}