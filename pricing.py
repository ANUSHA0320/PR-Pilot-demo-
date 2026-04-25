MAX_DISCOUNT_PERCENT = 50


def calculate_discount(price, discount_percent):
    capped_discount = max(0, min(discount_percent, MAX_DISCOUNT_PERCENT))
    return price * (capped_discount / 100)


def calculate_final_price(price, discount_percent):
    return price - calculate_discount(price, discount_percent)