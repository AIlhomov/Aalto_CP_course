#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#define fastio                    \
    std::ios::sync_with_stdio(0); \
    std::cin.tie(0);              \
    std::cout.tie(0);

class manacher
{
public:
    std::string ms;
    std::vector<int> p;

    manacher(const std::string &s)
    {
        ms = "@";
        for (char c : s)
        {
            ms += "#" + std::string(1, c);
        }
        ms += "#$";
        p.assign(ms.size(), 0);
        runManacher();
    }

    void runManacher()
    {
        int n = (int)ms.size();
        int l = 0, r = 0;

        for (int i = 1; i < n - 1; ++i)
        {
            int mirror = l + r - i;
            if (0 <= mirror && mirror < n)
            {
                p[i] = std::max(0, std::min(r - i, p[mirror]));
            }
            else
            {
                p[i] = 0;
            }

            while (i + 1 + p[i] < n && i - 1 - p[i] >= 0 && ms[i + 1 + p[i]] == ms[i - 1 - p[i]])
            {
                p[i]++;
            }

            if (i + p[i] > r)
            {
                l = i - p[i];
                r = i + p[i];
            }
        }
    }

    int getLongest(int cen, bool odd)
    {
        int pos = 2 * cen + 2 + (odd ? 0 : 1);
        return p[pos];
    }

    bool check(int l, int r)
    {
        int length = r - l + 1;
        return length <= getLongest((l + r) / 2, length % 2);
    }
};

std::string getLongestPal(const std::string &s)
{
    int n = (int)s.size();
    int maxLen = 1;
    int start = 0;
    manacher M(s);

    for (int i = 0; i < n; ++i)
    {
        int oddLen = M.getLongest(i, true);
        if (oddLen > maxLen)
        {
            start = i - (oddLen - 1) / 2;
        }

        int evenLen = M.getLongest(i, false);
        if (evenLen > maxLen)
        {
            start = i - (evenLen - 1) / 2;
        }

        maxLen = std::max(maxLen, std::max(oddLen, evenLen));
    }

    return s.substr(start, maxLen);
}
// g++ d.cpp -o d -std=c++17
int main()
{
    fastio;
    std::string s;
    std::getline(std::cin, s);
    std::cout << getLongestPal(s) << std::endl;
    return 0;
}