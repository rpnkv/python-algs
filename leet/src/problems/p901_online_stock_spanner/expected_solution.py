class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        stack = self.stack

        if not stack:
            stack.append((price, 1))
            return 1

        if stack[-1][0] > price:
            stack.append((price, 1))
            return 1
        else:
            len_sum = 0
            while stack and stack[-1][0] <= price:
                old_price, old_len = stack.pop()
                len_sum+=old_len

            stack.append((price, len_sum + 1))

            return stack[-1][1]