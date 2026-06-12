class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        stack = self.stack

        if not stack:
            stack.append((price, 1))
        else:
            count = 1
            while stack and stack[-1][0] <= price:
                count += stack.pop()[1]
            stack.append((price, count))

        return stack[-1][1]


if __name__ == "__main__":
    cases = [
        ([5, 5, 6], [1, 2, 3], "my example 1"),
        ([100, 80, 60, 70, 60, 75, 85], [1, 1, 1, 2, 1, 4, 6], "example 1")
    ]

    for incoming, expected_outcome, case_id in cases:
        print()
    print("checking case: '" + case_id + "':")
    s = StockSpanner()
    for i in range(len(incoming)):
        inc, exp_out = incoming[i], expected_outcome[i]

    act_out = s.next(inc)

    assert act_out == exp_out, "Failed for pos: '" + str(i) + "'"

    print("------ SUCCESS ------")
