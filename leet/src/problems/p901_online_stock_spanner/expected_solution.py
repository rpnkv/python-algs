class StockSpanner:

    def __init__(self):
        self.archive_prices=[]

    def next(self, price: int) -> int:
        archive_prices = self.archive_prices

        if not archive_prices:
            archive_prices.append(price)
            return 1

        if archive_prices[-1] <= price:
            archive_prices.append(price)
            return len(archive_prices)
        else:
            archive_price = archive_prices.pop()
            while archive_prices and archive_price > price:


        raise NotImplementedError
