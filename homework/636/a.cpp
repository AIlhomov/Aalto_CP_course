#include <bits/stdc++.h>

#define ll long long
#define fast_io()                 \
    std::ios::sync_with_stdio(0); \
    std::cin.tie(0);              \
    std::cout.tie(0);
using namespace std;

int main()
{
    fast_io();

    ll n, x;
    cin >> n >> x;
    vector<ll> a(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> a[i];
    }

    map<ll, ll> Map;
    Map[0] = 1;
    ll currSum = 0;
    ll res = 0;

    for (int i = 0; i < n; ++i)
    {
        currSum += a[i];

        if (Map.find(currSum - x) != Map.end())
        {
            res += Map[currSum - x];
        }

        Map[currSum]++;
    }

    cout << res << endl;

    return 0;
}