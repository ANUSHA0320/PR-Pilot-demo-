from pricing import calculate_final_price


def display_invoice(price, discount_percent):
    final_price = calculate_final_price(price, discount_percent)

    print("Invoice Preview")
    print(f"Original price: ${price:.2f}")
    print(f"Discount: {discount_percent}%")
    print(f"Final price: ${final_price:.2f}")


if __name__ == "__main__":
    display_invoice(100, 10)