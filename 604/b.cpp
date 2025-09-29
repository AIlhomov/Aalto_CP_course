#include <bits/stdc++.h>
using namespace std;
#define ll long long

bool compare(string a, string b)
{
    return (a + b < b + a);
}

string lexSmallest(string a[], ll n)
{
    sort(a, a + n, compare);

    string answer = "";
    for (ll i = 0; i < n; i++)
        answer += a[i];

    return answer;
}

int main()
{
    ll n;
    cin >> n;
    string a[n];
    for (ll i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    cout << lexSmallest(a, n) << endl;
    return 0;
}