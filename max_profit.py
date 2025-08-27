def max_profit(prices):
    max_profit = 0
    i = 0
    j = i + 1

    while j < len(prices):
        if prices[i] < prices[j]:
            max_profit = max(max_profit, prices[j] - prices[i])
        else:
            i = j

        j += 1

    return max_profit


print(max_profit([10, 1, 5, 6, 7, 1]))
print(max_profit([10, 8, 7, 5, 2]))
