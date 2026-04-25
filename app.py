from config import APP_NAME, CURRENCY, DEFAULT_DISCOUNT
from pricing import calculate_final_price


def display_invoice(price, discount_percent=DEFAULT_DISCOUNT, promo_code=None):
    final_price = calculate_final_price(price, discount_percent)

    if promo_code == "SPRING25":
        final_price *= 0.75

    print(APP_NAME)
    print(f"Original price: {price:.2f} {CURRENCY}")
    print(f"Discount: {discount_percent}%")
    print(f"Final price: {final_price:.2f} {CURRENCY}")


if __name__ == "__main__":
    display_invoice(100, 10, "SPRING25")