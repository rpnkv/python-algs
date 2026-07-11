class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        mask = 0b01

        carry = place = 0

        while a or b or carry:
            a_bit = a & mask
            b_bit = b & mask

            if a_bit & b_bit & carry:
                carry = 0b01
                res_mask = 0b01
            elif a_bit & b_bit:
                carry = 0b01
                res_mask = 0b00
            elif (a_bit | b_bit) & carry:
                carry = 0b01
                res_mask = 0b00
            elif a_bit | b_bit | carry:
                carry = 0b00
                res_mask = 0b01
            else:
                carry = 0b00
                res_mask = 0b00

            res_mask <<= place

            res |= res_mask

            a >>= 1
            b >>= 1
            place += 1

        return res


if __name__ == "__main__":
    cases = [
        (1, 2, 3, "ex 1N"),
        (4, 7, 11, "ex 2N"),
        (1, 2, 3, "ex 1L"),
        (2, 3, 5, "ex 2L"),
        (4, 5, 9, "cs 6L"),
    ]

    for i1, i2, e, case_id in cases[4:]:
        a = Solution().getSum(i1, i2)

        assert a == e, f"failed case {case_id}; a/e: {a}/{e}"
