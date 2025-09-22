// g++ -std=c++17 -O2 -pipe -Wall -Wextra c.cpp -o a
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1'000'000'007;
const int INF = 1e9;
#define ll long long
#define fast                     \
    ios::sync_with_stdio(false); \
    cin.tie(nullptr);

vector<int> longestSubarray(vector<int> &A, int limit)
{
    deque<int> maxd, mind;
    int i = 0, j;
    for (j = 0; j < A.size(); ++j)
    {
        while (!maxd.empty() && A[j] > maxd.back())
            maxd.pop_back();
        while (!mind.empty() && A[j] < mind.back())
            mind.pop_back();
        maxd.push_back(A[j]);
        mind.push_back(A[j]);
        if (maxd.front() - mind.front() > limit)
        {
            if (maxd.front() == A[i])
                maxd.pop_front();
            if (mind.front() == A[i])
                mind.pop_front();
            ++i;
        }
    }
    vector<int> res;
    res.push_back(i);
    res.push_back(j - i);
    return res;
}

int main()
{
    int n, x;
    cin >> n >> x;
    vector<int> a(n);

    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    vector<int> res = longestSubarray(a, x);
    cout << res[0] + 1 << " " << res[1]; // index, length
    return 0;
}