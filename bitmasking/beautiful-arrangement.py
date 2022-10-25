def count_set_bits(mask):
    b = bin(mask)
    return b.count('1')

def assign(N, cost):
    dp = [0]

    for i in range(pow(2,N)):
        dp.append(float('inf'))
    
    dp[0] = 0
    
    for mask in range(pow(2, N)):
        x = count_set_bits(mask)
        for j in range(N):
            if i & (1 << j):
                dp[mask|(1<<j)] = min(dp[mask|(1<<j)], dp[mask]+cost[x-1][j-1])
    
    return dp[pow(2,N)-1]


if __name__ == "__main__":
    N = 3
    cost = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    print(assign(N, cost))