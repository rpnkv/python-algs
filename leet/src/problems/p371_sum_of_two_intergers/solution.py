class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        mask = 0b01

        carry = 0

        for pos in range(32):
            a_bit = a & mask
            b_bit = b & mask

            if not (a | b | carry):
                break

            x = a_bit ^ b_bit ^ carry
            carry = (a_bit & b_bit) | (a_bit & carry) | (b_bit & carry)

            x <<= pos
            a >>= 1
            b >>= 1
            res |= x

        if res & 0x80000000:
            return ~(res ^ 0xFFFFFFFF)

        return res


if __name__ == "__main__":
    cases = [
        (1, 2, 3, "ex 1N"),
        (4, 7, 11, "ex 2N"),
        (1, 2, 3, "ex 1L"),
        (2, 3, 5, "ex 2L"),
        (4, 5, 9, "cs 6L"),
    ]

    for i1, i2, e, case_id in cases:
        a = Solution().getSum(i1, i2)

        assert a == e, f"failed case {case_id}; a/e: {a}/{e}"
