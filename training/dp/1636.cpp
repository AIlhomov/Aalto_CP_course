#include <bits/stdc++.h>
using namespace std;

const int MOD = 1'000'000'007;
#define ll long long
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, x;
    cin >> n >> x;
    vector<int> coins(n);
    for (int &c : coins)
        cin >> c;

    vector<int> dp(x + 1, 0);
    dp[0] = 1;
    sort(coins.begin(), coins.end());
    for (int c : coins)
    {
        for (int s = c; s <= x; s++)
        {
            dp[s] += dp[s - c];
            if (dp[s] >= MOD)
                dp[s] -= MOD;
        }
    }
    cout << dp[x] << '\n';
    return 0;
}
