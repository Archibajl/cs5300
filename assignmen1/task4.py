
#calculates discounted price, uses price and discount percentage
def calculate_discount(price, discount):
    discountRate = discount / 100
    discountedPrice = price * discountRate
    return round(price - discountedPrice, 2)