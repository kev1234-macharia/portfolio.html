def calculate_discount(original_price, discount_percent):
    if discount_percent >= 20:
        discounted_price = original_price * (1 - discount_percent / 100)
        return discounted_price
    else:
        return original_price

original_price = 10000
discount = 35.2
final_price = calculate_discount(original_price, discount)
print("Final Price after applying discount:", final_price)

original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))


final_price = calculate_discount(original_price, discount_percent)


if final_price == original_price:
    print("No discount applied. Final price:", final_price)
else:
    print("Final price after applying discount:", final_price)