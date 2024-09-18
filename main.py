def calculate_discount(price, discount):
    if discount >= 20:
        new_price = price * (1 - (discount / 100))
    else:
        new_price = price
    return new_price


price_1 = int(input("Enter the original price of the item: "))
discount_1 = int(input("Enter the discount to be applied: "))
price = price_1
discount = discount_1
new_price = calculate_discount(price, discount)
print("The new price is:", new_price)
