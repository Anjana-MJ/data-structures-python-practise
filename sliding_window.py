def buy_and_sell_stocks(price):
    max_profit = 0
    min_value = price[0]
    profit = 0
    for i in range(1, len(price)):
        if min_value <= price[i]:
            profit = price[i] - min_value
        else:
            min_value = price[i]
        max_profit = max(max_profit, profit)
    return max_profit


print(buy_and_sell_stocks([7, 6, 4, 3, 1, 8]))

print(buy_and_sell_stocks([7, 6, 4, 3, 1]))
