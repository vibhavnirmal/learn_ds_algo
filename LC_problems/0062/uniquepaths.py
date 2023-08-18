def uniquePaths(m, n):
    """
    Correct: dp = [[1]*n for _ in range(m)]
    Wrong: dp = [[1]*n]*m 
    
    This line creates a 2D list with m rows and n columns, where each cell is initialized to 1. 

    However, the issue is that all rows of the dp matrix refer to the same list object, meaning that modifying any row will affect all other rows
    """
    dp = [[1]*n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]

if __name__ == "__main__":
    print(uniquePaths(3,7))