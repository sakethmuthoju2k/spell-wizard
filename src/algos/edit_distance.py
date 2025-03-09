"""
Calculate the Damerau - Levenshtein (edit) distance between two words
"""

class EditDistance:
    def __init__(self):
        pass

    def get_edit_distance(self, word1, word2):
        m, n = len(word1), len(word2)

        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = i
        
        for j in range(n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif i>1 and j>1 and word1[i-1] == word2[j-2] and word1[i-2] == word2[j-1]:
                    dp[i][j] = 1 + min(dp[i-2][j-2], dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        
        return dp[m][n]

