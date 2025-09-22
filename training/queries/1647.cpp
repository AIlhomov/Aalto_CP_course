// g++ -std=c++17 -O2 -pipe -Wall -Wextra a.cpp -o a
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1'000'000'007;
const int INF = 1e9;
#define ll long long
#define fast                     \
    ios::sync_with_stdio(false); \
    cin.tie(nullptr);

struct SegmentTree
{
    int n;
    vector<ll> seg;

    SegmentTree(const vector<ll> &a)
    {
        n = (int)a.size();
        seg.assign(4 * n, INF);
        build(0, 0, n - 1, a);
    }

    void build(int node, int l, int r, const vector<ll> &a)
    {
        if (l == r)
        {
            seg[node] = a[l];
            return;
        }
        int mid = (l + r) / 2;
        int left = 2 * node + 1;  // left child
        int right = 2 * node + 2; // right child
        build(left, l, mid, a);
        build(right, mid + 1, r, a);
        seg[node] = min(seg[left], seg[right]);
    }

    void update(int idx, ll val)
    {
        update(0, 0, n - 1, idx, val);
    }

    void update(int node, int l, int r, int idx, ll val)
    {
        if (l == r)
        {
            seg[node] = val;
            return;
        }
        int mid = (l + r) / 2;
        int left = 2 * node + 1;
        int right = 2 * node + 2;
        if (idx <= mid)
        {
            update(left, l, mid, idx, val);
        }
        else
        {
            update(right, mid + 1, r, idx, val);
        }
        seg[node] = min(seg[left], seg[right]);
    }

    // minimum range on [ql, qr]
    ll query(int ql, int qr)
    {
        return query(0, 0, n - 1, ql, qr);
    }

    ll query(int node, int l, int r, int ql, int qr)
    {
        if (qr < l || r < ql)
            return INF;
        if (ql <= l && r <= qr)
            return seg[node];
        // partial part
        int mid = (l + r) / 2;
        int left = 2 * node + 1;
        int right = 2 * node + 2;
        return min(query(left, l, mid, ql, qr),
                   query(right, mid + 1, r, ql, qr));
    }
};

int main()
{
    int n, q;
    cin >> n >> q;
    vector<ll> a;
    a.resize(n);
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    SegmentTree st(a);
    while (q--)
    {
        int l, r;
        cin >> l >> r;
        l--;
        r--;
        cout << st.query(l, r) << '\n';
    }
    return 0;
}