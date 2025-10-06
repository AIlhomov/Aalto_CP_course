#include <iostream>
#include <vector>
#define fastio()                  \
    std::ios::sync_with_stdio(0); \
    std::cin.tie(0);              \
    std::cout.tie(0);
using namespace std;
#define ll long long

int main()
{
    fastio();
    ll n, q;
    cin >> n >> q;
    vector<ll> k(n);
    vector<ll> x(q);

    for (int i = 0; i < n; ++i)
    {
        cin >> k[i];
    }
    for (int i = 0; i < q; ++i)
    {
        cin >> x[i];
    }

    for (int i = 0; i < q; ++i)
    {
        ll initial_key = x[i];
        ll inmate = k[initial_key - 1];

        ll res = 1;
        while (initial_key != inmate)
        {
            inmate = k[inmate - 1];
            ++res;
        }
        cout << res << " ";
    }

    return 0;
}