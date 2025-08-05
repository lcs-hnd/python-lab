# 121 v1 - best time to buy and sell stocks
prices = [7,1,5,3,6,4]

def algo(prices):
  buy = 0
  sell = 1
  max_profit = 0
  
  while sell < len(prices):
    if prices[sell] > prices[buy]:
      max_profit = max(max_profit, prices[sell] - prices[buy])
    else:
      buy = sell
    sell +=1
  return max_profit

print(algo(prices))
