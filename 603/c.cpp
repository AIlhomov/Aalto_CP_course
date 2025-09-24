#include <bits/stdc++.h>
using namespace std;

const int MOD = 1'000'000'007;
const long long INF = 1e18;
using ll = long long;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];
    if (is_sorted(a.begin(), a.end()))
    {
        cout << 0 << "\n";
        return 0;
    }
    ll res = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n - 1; j++)
            if (a[j] > a[j + 1])
            {
                swap(a[j], a[j + 1]);
                res++;
            }

    cout << res << "\n";
    return 0;
}
