DISSCOUNT_RATE = 3

def MaximumDiscount(N, price):
    price.sort(reverse = True)
    discount = price[DISSCOUNT_RATE-1::DISSCOUNT_RATE]
    return sum(discount)


