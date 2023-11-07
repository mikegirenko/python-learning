"""
You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product.
You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars),
and the starting inventory. Return the total profit made, rounded to the nearest dollar.
"""

profit_1 = {"cost_price": 32.67, "sell_price": 45.00, "inventory": 1200}  # ➞ 14796
profit_2 = {"cost_price": 225.89, "sell_price": 550.00, "inventory": 100}  # ➞ 32411
profit_3 = {"cost_price": 2.77, "sell_price": 7.95, "inventory": 8500}  # ➞ 44030


def calculate_profit(this_profit) -> int:
    one_unit_profit = this_profit["sell_price"] - this_profit["cost_price"]
    total_profit = one_unit_profit * this_profit["inventory"]

    return round(total_profit)


assert calculate_profit(profit_1) == 14796
assert calculate_profit(profit_2) == 32411
assert calculate_profit(profit_3) == 44030
