prices  = [100,90,50]

discount_price = 10

final_prices = []
for price in prices:
    final_price = price -(price * discount_price/100)
    final_prices.append(final_price)

print(final_prices)