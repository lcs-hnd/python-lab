# 121 v2 - best time to buy and sell stocks
prices = [7,1,5,3,6,4]

def algo(prices):
  min_price = prices[0]
  max_profit = 0
  for price in prices[1:]:
    max_profit = max(max_profit, price - min_price)
    min_price = min(min_price, price)
  return max_profit

print(algo(prices))