// g++ -std=c++17 -O2 -pipe -Wall -Wextra a.cpp -o a
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1'000'000'007;
const int INF = 1e9;
#define ll long long
#define fast                     \
    ios::sync_with_stdio(false); \
    cin.tie(nullptr);

struct FenwickTree
{
    vector<ll> bit; // binary indexed tree
    int n;

    FenwickTree(int n)
    {
        this->n = n;
        bit.assign(n, 0);
    }

    FenwickTree(vector<int> const &a) : FenwickTree(a.size())
    {
        for (size_t i = 0; i < a.size(); i++)
            add(i, a[i]);
    }

    ll sum(int r)
    {
        ll ret = 0;
        for (; r >= 0; r = (r & (r + 1)) - 1)
            ret += bit[r];
        return ret;
    }

    ll sum(int l, int r)
    {
        return sum(r) - sum(l - 1);
    }

    void add(int idx, int delta)
    {
        for (; idx < n; idx = idx | (idx + 1))
            bit[idx] += delta;
    }
    void range_add(int l, int r, int val)
    {
        add(l, val);
        add(r + 1, -val);
    }
};

int main()
{
    fast;

    int n, q;
    cin >> n >> q;
    vector<ll> a(n + 1);
    for (int i = 0; i < n; ++i)
        cin >> a[i];

    FenwickTree fw(n);

    while (q--)
    {
        int type;
        cin >> type;
        if (type == 1)
        {
            int k, r;
            ll u;
            cin >> k >> r >> u;
            k--;
            r--;
            fw.range_add(k, r, u);
        }
        else
        {
            int l;
            cin >> l;
            l--;
            cout << (a[l] + fw.sum(l)) << '\n';
        }
    }

    return 0;
}
