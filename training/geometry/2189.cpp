#include <bits/stdc++.h>

#define ll long long
#define fastio()             \
    ios::sync_with_stdio(0); \
    cin.tie(0);              \
    cout.tie(0);

using namespace std;

int main()
{
    fastio();
    int t;
    if (!(cin >> t))
        return 0;
    while (t--)
    {
        ll x1, y1, x2, y2, x3, y3;
        cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
        ll cross = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1);
        if (cross > 0)
            cout << "LEFT\n";
        else if (cross < 0)
            cout << "RIGHT\n";
        else
            cout << "TOUCH\n";
    }
    return 0;
}
