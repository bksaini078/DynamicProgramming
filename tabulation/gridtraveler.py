# details are present in memoization gridtraveler
def gridTraveler(m, n):
    table = [[0] * (n + 1) for i in range(m + 1)]
    table[1][1] = 1
    print(table)

    for i in range(m + 1):
        # adding to right
        for j in range(n + 1):
            if j <= n - 1:
                table[i][j + 1] += table[i][j]
            if i <= m - 1:
                table[i + 1][j] += table[i][j]
            # print(table)

    return table[m][n]


if __name__ == '__main__':
    print(gridTraveler(3, 3))
    print(gridTraveler(1, 1))
    print(gridTraveler(3, 2))
    print(gridTraveler(5, 5))
    print(gridTraveler(18, 18))

    # print(table[1][1])
