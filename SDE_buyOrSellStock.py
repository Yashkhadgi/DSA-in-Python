def maxProfit(prices):

    # Lowest buying price seen so far
    min_price = prices[0]

    # Maximum profit found so far
    max_profit = 0

    # Traverse prices
    for price in prices:

        # Update minimum price
        if price < min_price:
            min_price = price

        # Profit if sold today
        profit = price - min_price

        # Update answer
        if profit > max_profit:
            max_profit = profit

    return max_profit


# User input
prices = list(map(int, input("Enter stock prices separated by spaces: ").split()))

answer = maxProfit(prices)

print("Maximum Profit =", answer)