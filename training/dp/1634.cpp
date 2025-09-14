// g++ -std=c++17 -O2 -pipe -Wall -Wextra coins.cpp -o coins
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1'000'000'007;
const int INF = 1e9;
#define ll long long

// for the problem: (book)
// bool ready[N];
//    int value[N];
// is the same as:
vector<int> coins, value;
vector<char> ready;

int solve(int x)
{
    if (x < 0)
        return INF;
    if (x == 0)
        return 0;
    if (ready[x])
        return value[x];
    int best = INF;
    for (auto c : coins)
        best = min(best, solve(x - c) + 1);
    value[x] = best;
    ready[x] = true;
    return best;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll n, x;
    cin >> n >> x;
    coins.resize(n);
    for (int i = 0; i < n; i++)
        cin >> coins[i];
    // extra (not mentioned):
    value.assign(x + 1, INF);
    ready.assign(x + 1, 0);
    int ans = solve(x);
    cout << (ans == INF ? -1 : ans) << '\n'; // if statement to print -1 or the ans
    return 0;
}
