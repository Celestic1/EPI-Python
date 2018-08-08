'''
Get maximum profit from buying and selling one share of stock
Can't sell before buying
A = [310,315,275,295,260,270,290,230,255,250]
Max Profit = 30
'''

def buy_and_sell_stock_once(prices):
   
    if not prices or len(prices) == 1:
        return 0

    min_price = prices[0]
    max_profit = prices[1] - prices[0]
    for price in prices[1:]:
        min_price = min(min_price,price)
        curr_profit = price - min_price
        max_profit = max(max_profit,curr_profit)
    return max_profit
