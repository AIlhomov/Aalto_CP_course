#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);

static inline int bitlen(unsigned x)
{
    return x ? 32 - __builtin_clz(x) : 1;
}
struct Item
{
    unsigned v;
    int bl;
};

int main()
{
    fastio;

    int n;
    if (!(cin >> n))
        return 0;
    vector<unsigned> a(n);
    for (auto &x : a)
        cin >> x;

    vector<Item> v;
    v.reserve(n);
    for (auto x : a)
        v.push_back({x, bitlen(x)});
    sort(v.begin(), v.end(), [](const Item &L, const Item &R)
         {
        if (L.bl != R.bl) return L.bl > R.bl;
        return L.v > R.v; });

    int best = -1;
    unsigned X = 0, Y = 0;

    for (int i = 0; i < n; ++i)
    {
        if (2 * v[i].bl <= best)
            break; // outer prune
        for (int j = i + 1; j < n; ++j)
        {
            if (v[i].bl + v[j].bl <= best)
                break;                                        // inner prune
            unsigned long long prod = 1ULL * v[i].v * v[j].v; // fits in 64-bit
            int ones = __builtin_popcountll(prod);
            if (ones > best)
            {
                best = ones;
                X = v[i].v;
                Y = v[j].v;
            }
        }
    }

    cout << best << "\n"
         << X << " " << Y << "\n";
    return 0;
}
