class StockSpanner:

    def __init__(self):
        self.prices=[]

    def next(self, price: int) -> int:
        count = 0

        for archive_price in reversed(self.prices):
            if archive_price <= price:
                count += 1
            else:
                break

        self.prices.append(price)

        return count + 1