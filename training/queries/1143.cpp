// g++ -std=c++17 -O2 -pipe -Wall -Wextra hotels.cpp -o hotels
#include <bits/stdc++.h>
using namespace std;

struct SegTreeMax
{
    int n;
    vector<long long> seg; // maximum in range
    vector<long long> a;   // current values

    SegTreeMax(const vector<long long> &init)
    {
        n = (int)init.size();
        a = init;
        seg.assign(4 * n, 0);
        build(0, 0, n - 1);
    }

    void build(int node, int l, int r)
    {
        if (l == r)
        {
            seg[node] = a[l];
            return;
        }
        int mid = (l + r) / 2;
        int L = 2 * node + 1, R = 2 * node + 2;
        build(L, l, mid);
        build(R, mid + 1, r);
        seg[node] = max(seg[L], seg[R]);
    }

    // find first index with value >= need, or -1 if none
    int first_at_least(long long need)
    {
        if (seg[0] < need)
            return -1;
        return first_at_least(0, 0, n - 1, need);
    }

    int first_at_least(int node, int l, int r, long long need)
    {
        if (l == r)
            return l;
        int mid = (l + r) / 2;
        int L = 2 * node + 1, R = 2 * node + 2;
        if (seg[L] >= need)
            return first_at_least(L, l, mid, need);
        return first_at_least(R, mid + 1, r, need);
    }

    // set position idx to newVal
    void set_val(int idx, long long newVal) { set_val(0, 0, n - 1, idx, newVal); }

    void set_val(int node, int l, int r, int idx, long long newVal)
    {
        if (l == r)
        {
            seg[node] = a[l] = newVal;
            return;
        }
        int mid = (l + r) / 2;
        int L = 2 * node + 1, R = 2 * node + 2;
        if (idx <= mid)
            set_val(L, l, mid, idx, newVal);
        else
            set_val(R, mid + 1, r, idx, newVal);
        seg[node] = max(seg[L], seg[R]);
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<long long> h(n);
    for (int i = 0; i < n; ++i)
        cin >> h[i];

    SegTreeMax st(h);

    // Answer queries
    for (int i = 0; i < m; ++i)
    {
        long long r;
        cin >> r;
        int idx = st.first_at_least(r); // 0-based index or -1
        if (idx == -1)
        {
            cout << 0 << (i + 1 == m ? '\n' : ' ');
        }
        else
        {
            long long newVal = st.a[idx] - r;
            st.set_val(idx, newVal);
            cout << (idx + 1) << (i + 1 == m ? '\n' : ' ');
        }
    }
    return 0;
}
