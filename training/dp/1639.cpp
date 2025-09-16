#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int solve(const string &word1, const string &word2)
{
    int n = word1.size();
    int m = word2.size();

    // Create DP cache
    vector<vector<int>> cache(n + 1, vector<int>(m + 1, 0));

    // Base cases: edit distance when one string is empty
    for (int j = 0; j <= m; j++)
        cache[n][j] = m - j;
    for (int i = 0; i <= n; i++)
        cache[i][m] = n - i;

    // Bottom-up DP calculation
    for (int i = n - 1; i >= 0; i--)
    {
        for (int j = m - 1; j >= 0; j--)
        {
            if (word1[i] == word2[j])
            {
                cache[i][j] = cache[i + 1][j + 1];
            }
            else
            {
                cache[i][j] = 1 + min({
                                      cache[i + 1][j],    // Remove
                                      cache[i][j + 1],    // Insert
                                      cache[i + 1][j + 1] // Replace
                                  });
            }
        }
    }

    return cache[0][0];
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string word1, word2;
    cin >> word1 >> word2;

    cout << solve(word1, word2) << "\n";

    return 0;
}
