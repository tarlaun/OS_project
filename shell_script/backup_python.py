import sys


def LCSubStr(s, t):
    # Create DP table
    n = len(s)
    m = len(t)
    dp = [[0 for i in range(m + 1)] for j in range(2)]
    res = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (s[i - 1] == t[j - 1]):
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1
                if (dp[i % 2][j] > res):
                    res = dp[i % 2][j]
            else:
                dp[i % 2][j] = 0
    return res




inputstr = sys.argv[1]
app_list = sys.argv[2:]

final_app = ""
max_len = 0

for app in app_list:
    lcs = LCSubStr(str(app), str(inputstr))
    if lcs > max_len:
        max_len = lcs
        final_app = str(app)

if max_len < int(len(inputstr) * 3 / 4):
    print("no_match")
else:
    print(final_app)

