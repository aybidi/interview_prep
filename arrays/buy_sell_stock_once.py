def buy_sell_stock_once(prices):
    min_price_so_far, max_profit_so_far = float('inf'), 0
    for price in prices:
        min_price_so_far = min(price, min_price_so_far)
        max_profit_so_far = max(max_profit_so_far, price - min_price_so_far)
    return max_profit_so_far

# print(buy_sell_stock_once([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
print(buy_sell_stock_once([310, 297]))