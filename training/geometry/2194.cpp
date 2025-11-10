#include <bits/stdc++.h>

#define ll long long
#define fastio()             \
    ios::sync_with_stdio(0); \
    cin.tie(0);              \
    cout.tie(0);

using namespace std;

struct P
{
    ll x, y;
};

static inline ll dist2(const P &a, const P &b)
{
    ll dx = a.x - b.x, dy = a.y - b.y;
    return dx * dx + dy * dy;
}

ll solve(vector<P> &pts)
{
    int n = (int)pts.size();
    vector<P> buf(n);

    function<ll(int, int)> rec = [&](int l, int r) -> ll
    {
        if (r - l <= 3)
        {
            ll d = LLONG_MAX;
            for (int i = l; i < r; i++)
                for (int j = i + 1; j < r; j++)
                    d = min(d, dist2(pts[i], pts[j]));
            sort(pts.begin() + l, pts.begin() + r, [](const P &a, const P &b)
                 { return a.y < b.y; });
            return d;
        }
        int m = (l + r) >> 1;
        ll midx = pts[m].x;

        ll dl = rec(l, m);
        ll dr = rec(m, r);
        ll d = min(dl, dr);

        merge(pts.begin() + l, pts.begin() + m, pts.begin() + m, pts.begin() + r,
              buf.begin(), [](const P &a, const P &b)
              { return a.y < b.y; });
        copy(buf.begin(), buf.begin() + (r - l), pts.begin() + l);

        int sz = 0;
        for (int i = l; i < r; i++)
            if ((pts[i].x - midx) * (pts[i].x - midx) < d)
                buf[sz++] = pts[i];

        for (int i = 0; i < sz; i++)
        {
            for (int j = i + 1; j < sz && (buf[j].y - buf[i].y) * (buf[j].y - buf[i].y) < d; j++)
            {
                d = min(d, dist2(buf[i], buf[j]));
            }
        }
        return d;
    };

    return rec(0, n);
}

int main()
{
    fastio();

    int n;
    if (!(cin >> n))
        return 0;
    vector<P> pts(n);
    for (int i = 0; i < n; i++)
        cin >> pts[i].x >> pts[i].y;

    sort(pts.begin(), pts.end(), [](const P &a, const P &b)
         {
        if (a.x != b.x) return a.x < b.x;
        return a.y < b.y; });

    ll d2 = solve(pts);
    cout.setf(std::ios::fixed);
    cout << setprecision(6) << sqrt((long double)d2) << "\n";
    return 0;
}
