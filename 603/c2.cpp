#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define INF 1e9

struct MergeSortTree
{
    int n;
    vector<vector<ll>> seg;

    MergeSortTree(const vector<ll> &a)
    {
        n = (int)a.size();
        seg.resize(4 * n);
        build(0, 0, n - 1, a);
    }

    void build(int node, int l, int r, const vector<ll> &a)
    {
        if (l == r)
        {
            seg[node] = {a[l]};
            return;
        }
        int mid = (l + r) / 2;
        int left = 2 * node + 1;
        int right = 2 * node + 2;
        build(left, l, mid, a);
        build(right, mid + 1, r, a);

        seg[node].resize(seg[left].size() + seg[right].size());
        std::merge(seg[left].begin(), seg[left].end(),
                   seg[right].begin(), seg[right].end(),
                   seg[node].begin());
    }

    int countLessThan(int ql, int qr, ll x)
    {
        return countLessThan(0, 0, n - 1, ql, qr, x);
    }

    int countLessThan(int node, int l, int r, int ql, int qr, ll x)
    {
        if (qr < l || r < ql)
            return 0;
        if (ql <= l && r <= qr)
        {
            return std::lower_bound(seg[node].begin(), seg[node].end(), x) - seg[node].begin();
        }
        int mid = (l + r) / 2;
        int left = 2 * node + 1;
        int right = 2 * node + 2;
        return countLessThan(left, l, mid, ql, qr, x) +
               countLessThan(right, mid + 1, r, ql, qr, x);
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    std::cin >> n;
    std::vector<ll> A(n);
    for (int i = 0; i < n; ++i)
    {
        std::cin >> A[i];
    }

    MergeSortTree mst(A);
    int res = 0;
    for (int i = 0; i < n; i++)
    {
        res += mst.countLessThan(A[i - 1], A[i + 1], A[i]);
        // cout << mst.countLessThan(l, r, x) << "\n";
    }
    cout << res * 2 << '\n';
    return 0;
}